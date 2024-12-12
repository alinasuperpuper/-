class Database:
    def __init__(self):
        self._records = []

    @property
    def records(self):
        return self._records.copy()

    def clear(self):
        self._records.clear()

    def add_record(self, data):
        if not data:
            raise ValueError("Некорректные данные.")
        self._records.append(data)

    def edit_record(self, old_data, new_data):
        if old_data in self._records:
            index = self._records.index(old_data)
            self._records[index] = new_data

    def delete_record(self, data):
        if data in self._records:
            self._records.remove(data)

    def record_exists(self, data):
        return data in self._records
