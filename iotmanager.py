import json


class IoTManager:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def remove_part(self, part):
        if part in self.parts:
            self.parts.remove(part)

    def get_part(self, part_id):

        if len(self.parts) == 0:
            return None
        for part in self.parts:
            print(part)
            if part.part_id == part_id:
                return part
        return None

    def get_parts(self):
        return self.parts

    def get_parts_by_category(self, category):
        return [part for part in self.parts if part.category == category]

    def get_parts_by_stock(self, stock):
        return [part for part in self.parts if part.stock == stock]

    def get_parts_by_position(self, position):
        return [part for part in self.parts if part.position == position]

    # IMPORTANT: this is where we implement persistence: we are saving the state of the iotmanager
    # into a JSON file. This is a state serialization technique. By Duberly Guarnizo.
    def json_save(self, filename):
        # we have to delete the data in the file, so no duplicates are saved
        with open(filename, 'w') as f:
            f.write(json.dumps(self.parts, default=lambda o: o.__dict__, sort_keys=True, indent=4))

    # And this is where we implement persistence loading: we are loading the state of the iotmanager
    def json_load(self, filename):
        with open(filename, 'r') as f:
            self.parts = json.load(f)

    def compare_json(self, filename):
        with open(filename, 'r') as f:
            parts = json.load(f)
        return self.parts == parts
