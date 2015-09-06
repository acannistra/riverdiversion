import pandas as pd

class WaterData(object):
	def read_file(self, file):
		""" read file using Pandas csv reader, tab-separated """ 
		return pd.read_csv(file, sep='\t')

	def reindex(self, index):
		""" reindex the Pandas DataFrame using the index given """
		self.data = self.data.set_index(index)
		self.data.index = pd.to_datetime(self.data.index)

	def remove_columns(self, columns):
		""" remove columns from the dataframe, given list of column IDs """
		for c in columns:
			del self.data[c]

	def drop_row(self, index):
		""" drop row given index value of row to drop """
		self.data = self.data.drop(self.data.index[[index]])

	def __init__(self, file_path):
		self.filepath = file_path
		self.data = self.read_file(self.filepath)






	


		