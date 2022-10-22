from Modules.SearchImageModule import *
from Modules.ImageBlockTemplate import *


class DisplayImages(ABC):
    @staticmethod
    def displayInTable(current_path, table_widget, image_path_list):
        table_widget.clear()
        column_number = 0
        row_number = 0

        table_widget.setRowCount((len(image_path_list) // 6) + 1)
        table_widget.setColumnCount(6)
        if image_path_list is not None:
            for current_path in image_path_list:
                cell_widget = ImageBlockTemplate.CreateImageBlockTemplate(current_path)
                if cell_widget is not None:
                    table_widget.setColumnWidth(column_number, 250)
                    table_widget.setRowHeight(row_number, 250)
                    table_widget.setCellWidget(row_number, column_number, cell_widget.GetImageBlockTemplate())
                    if column_number == 6:
                        row_number += 1
                        column_number = 0
                    else:
                        column_number += 1
                else:
                    print("go fuck yourself this is None")
        else:
            print("go fuck yourself this is None")
