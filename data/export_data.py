# *** TASK 15 ***
import datetime
import os
import process
import tui


class ExportData:
    def __init__(self, data, export_dir):
        # gets the data and the path data should be exported to
        self.data = data
        self.export_dir = export_dir
        self.header = ['Branch', 'Number of Reviews', 'Number of Positive Reviews', 'Average Review Score', 'Total Countries Reviewed']  # header for files

    @staticmethod
    def _aggregate_data(data):

        # to compile the needed data to be exported

        output_data = []

        for park in process.LIST_OF_BRANCHES:
            # park name, total num of reviews, number of positive reviews, ave rating, number of countries that reviewed branch
            output_data.append([
                park.capitalize(), len(process.get_reviews(park)), len(process.get_pos_reviews(park)), process.get_ave_rating(park), len(process.get_ave_reviews_by_loc(park))]
            )

        return output_data

    def export_as_txt(self):
        # to export as txt
        output_data = self._aggregate_data(self.data)

        with open(os.path.join(self.export_dir, 'export.txt'), "w") as file:
            file.write(f'{self.header[0]}, {self.header[1]}, {self.header[2]}, {self.header[3]}, {self.header[4]}, \n')
            for line in output_data:
                file.write(f'{line[0]}, {line[1]}, {line[2]}, {line[3]}\n')
            tui.tell_user(f"Successfully exported data to {os.path.join(self.export_dir, 'export.txt')}!")

    def export_as_csv(self):
        # to export as csv
        output_data = self._aggregate_data(self.data)

        with open(os.path.join(self.export_dir, 'export.csv'), "w") as file:
            file.write(f'{self.header[0]}, {self.header[1]}, {self.header[2]}, {self.header[3]}, {self.header[4]}, \n')
            for line in output_data:
                file.write(f'{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}\n')
            tui.tell_user(f"Successfully exported data to {os.path.join(self.export_dir, 'export.csv')}!")

    def export_as_json(self):
        # to export as json
        output_data = self._aggregate_data(self.data)

        with open(os.path.join(self.export_dir, 'export.json'), "w") as file:
            file.write('[\n')
            current_park = 0
            for line in output_data:
                file.write(' {\n')
                file.write(f'  "{self.header[0]}": "{line[0]}",\n  "{self.header[1]}": {line[1]},\n  "{self.header[2]}": {line[2]},\n  "{self.header[3]}": {line[3]},\n  "{self.header[4]}": {line[4]}\n')
                current_park += 1

                if current_park == len(output_data):
                    file.write(' }\n')
                else:
                    file.write(' },\n')

            file.write(']')
            tui.tell_user(f"Successfully exported data to {os.path.join(self.export_dir, 'export.json')}!")

    def __str__(self):
        return self.data
