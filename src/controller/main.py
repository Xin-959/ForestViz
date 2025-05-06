import sys
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QApplication
from data_import import DataImportTab
from model_train import ModelTrainTab
from visualization import VisualizationTab
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)  # 忽略弃用警告

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建标签页容器
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # 初始化各标签页
        self.data_tab = DataImportTab()
        self.model_tab = ModelTrainTab()
        self.viz_tab = VisualizationTab()

        # 添加标签页
        self.tabs.addTab(self.data_tab, "数据导入")
        self.tabs.addTab(self.model_tab, "模型训练")
        self.tabs.addTab(self.viz_tab, "可视化")

        # 建立标签页间通信
        self.data_tab.data_loaded.connect(self.on_data_loaded)
        self.model_tab.parent_window = self
        self.viz_tab.parent_window = self

        # 窗口设置
        self.resize(800, 600)
        self.setWindowTitle("ForestViz - 随机森林交互式可视化工具")

    def on_data_loaded(self):
        """数据加载完成后的处理"""
        self.model_tab.setEnabled(True)


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"程序崩溃: {e}")
        import traceback
        traceback.print_exc()