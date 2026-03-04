from .file_writer import FileWriter

class ReportWriter():
    @staticmethod
    def write(report, writer=FileWriter):
        #logica...
        writer.write(report)