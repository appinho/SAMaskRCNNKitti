class DataAssociation(object):
    def __init__(self):
        pass

    # TODO: remember all assigned objects and dont assign an object twice
    def nearest_neighbor(self,object_list,tracking_list):
        association_list = []
        for track_index,track in enumerate(tracking_list):
            minimum_distance = 1000
            minimum_index = -1
            for object_index,object in enumerate(object_list):
                distance = self.get_euclidean_distance(track,object)
                if distance < minimum_distance:
                    minimum_distance = distance
                    minimum_index = object_index
            association_list.append((minimum_index,track_index))
        print association_list
        return association_list

    def get_euclidean_distance(self,track,object):
        return ( (track.x[0]-object.x[0])**2 +
            (track.x[1]-object.x[1])**2 )**0.5