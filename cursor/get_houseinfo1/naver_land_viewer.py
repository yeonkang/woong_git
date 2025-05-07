import sys
import json
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QTableWidget, QTableWidgetItem, 
                             QPushButton, QLabel, QComboBox, QLineEdit, 
                             QMessageBox, QDialog, QTextEdit)
from PySide6.QtCore import Qt

class HouseDetailDialog(QDialog):
    def __init__(self, house_data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("상세 정보")
        self.setMinimumWidth(400)
        
        layout = QVBoxLayout()
        
        # 상세 정보 표시
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        
        # 데이터 포맷팅
        details = f"""
        동: {house_data['buildingName']} 
        층: {house_data['floorInfo']}
        가격: {house_data['dealOrWarrantPrc']}
        면적: {house_data['areaName']}㎡
        방향: {house_data['direction']}
        거래유형: {house_data['tradeTypeName']}
        
        특징:
        {house_data['articleFeatureDesc']}
        
        태그:
        {', '.join(house_data['tagList'])}
        """
        
        text_edit.setText(details)
        layout.addWidget(text_edit)
        
        # 닫기 버튼
        close_btn = QPushButton("닫기")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)
        
        self.setLayout(layout)

class NaverLandViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("네이버 부동산 뷰어")
        self.setMinimumSize(1000, 600)
        
        # 데이터 로드
        try:
            with open('naver_land_data.json', 'r', encoding='utf-8') as f:
                self.house_data = json.load(f)['articleList']
        except Exception as e:
            QMessageBox.critical(self, "오류", f"데이터 로드 실패: {str(e)}")
            self.house_data = []
        
        self.init_ui()
        
    def init_ui(self):
        # 메인 위젯과 레이아웃
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # 필터 영역
        filter_layout = QHBoxLayout()
        
        # 거래유형 필터
        self.trade_type_combo = QComboBox()
        self.trade_type_combo.addItem("전체")
        self.trade_type_combo.addItem("매매")
        self.trade_type_combo.addItem("전세")
        filter_layout.addWidget(QLabel("거래유형:"))
        filter_layout.addWidget(self.trade_type_combo)
        
        # 가격 필터
        self.price_min_edit = QLineEdit()
        self.price_max_edit = QLineEdit()
        filter_layout.addWidget(QLabel("가격 범위:"))
        filter_layout.addWidget(self.price_min_edit)
        filter_layout.addWidget(QLabel("~"))
        filter_layout.addWidget(self.price_max_edit)
        
        # 면적 필터
        self.area_min_edit = QLineEdit()
        self.area_max_edit = QLineEdit()
        filter_layout.addWidget(QLabel("면적 범위:"))
        filter_layout.addWidget(self.area_min_edit)
        filter_layout.addWidget(QLabel("~"))
        filter_layout.addWidget(self.area_max_edit)
        
        # 필터 적용 버튼
        filter_btn = QPushButton("필터 적용")
        filter_btn.clicked.connect(self.apply_filters)
        filter_layout.addWidget(filter_btn)
        
        layout.addLayout(filter_layout)
        
        # 테이블 위젯
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "동", "층", "가격", "면적", "방향", "거래유형", "상세보기"
        ])
        self.table.horizontalHeader().setStretchLastSection(True)
        
        # 데이터 표시
        self.update_table()
        
        layout.addWidget(self.table)
        
    def update_table(self, filtered_data=None):
        data = filtered_data if filtered_data else self.house_data
        self.table.setRowCount(len(data))
        
        for row, house in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(house['buildingName']))
            self.table.setItem(row, 1, QTableWidgetItem(house['floorInfo']))
            self.table.setItem(row, 2, QTableWidgetItem(house['dealOrWarrantPrc']))
            self.table.setItem(row, 3, QTableWidgetItem(house['areaName']))
            self.table.setItem(row, 4, QTableWidgetItem(house['direction']))
            self.table.setItem(row, 5, QTableWidgetItem(house['tradeTypeName']))
            
            # 상세보기 버튼
            detail_btn = QPushButton("상세보기")
            detail_btn.clicked.connect(lambda checked, h=house: self.show_detail(h))
            self.table.setCellWidget(row, 6, detail_btn)
    
    def show_detail(self, house_data):
        dialog = HouseDetailDialog(house_data, self)
        dialog.exec()
    
    def apply_filters(self):
        filtered_data = self.house_data.copy()
        
        # 거래유형 필터
        trade_type = self.trade_type_combo.currentText()
        if trade_type != "전체":
            filtered_data = [h for h in filtered_data if h['tradeTypeName'] == trade_type]
        
        # 가격 필터
        try:
            price_min = int(self.price_min_edit.text().replace("억", "").replace(",", "")) if self.price_min_edit.text() else 0
            price_max = int(self.price_max_edit.text().replace("억", "").replace(",", "")) if self.price_max_edit.text() else float('inf')
            
            def get_price(price_str):
                if "억" in price_str:
                    return int(price_str.replace("억", "").replace(",", "")) * 10000
                return int(price_str.replace(",", ""))
            
            filtered_data = [h for h in filtered_data if price_min <= get_price(h['dealOrWarrantPrc']) <= price_max]
        except ValueError:
            pass
        
        # 면적 필터
        try:
            area_min = float(self.area_min_edit.text()) if self.area_min_edit.text() else 0
            area_max = float(self.area_max_edit.text()) if self.area_max_edit.text() else float('inf')
            filtered_data = [h for h in filtered_data if area_min <= float(h['area1']) <= area_max]
        except ValueError:
            pass
        
        self.update_table(filtered_data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NaverLandViewer()
    window.show()
    sys.exit(app.exec()) 