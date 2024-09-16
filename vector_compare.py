import numpy as np
from scipy.spatial.distance import euclidean, cosine

# Hàm tính khoảng cách Euclidean giữa hai vector
def euclidean_distance(v1, v2):
    return euclidean(v1, v2)

# Hàm tính khoảng cách Cosine giữa hai vector
def cosine_distance(v1, v2):
    return cosine(v1, v2)

# Hàm tính khoảng cách giữa v và các lớp
def calculate_distances(v, data, distance_metric='euclidean'):
    distances_to_classes = []
    
    # Lặp qua từng lớp
    for class_idx, class_vectors in enumerate(data):
        distances = []
        
        # Lặp qua từng vector trong lớp
        for vector in class_vectors:
            # Tính khoảng cách giữa vector v và vector trong lớp
            if distance_metric == 'euclidean':
                dist = euclidean_distance(v, vector)
            elif distance_metric == 'cosine':
                dist = cosine_distance(v, vector)
            else:
                raise ValueError('Unknown distance metric')
            
            distances.append(dist)
        
        # Lấy khoảng cách trung bình của v đến các vector trong lớp
        avg_distance = np.mean(distances)
        distances_to_classes.append(avg_distance)
    
    return distances_to_classes

# Dữ liệu các vector theo lớp
data = [
    [[1, 2], [2, 3], [3, 4]],  # Lớp 0
    [[5, 5], [6, 7], [7, 8]],  # Lớp 1
    [[9, 10], [10, 11], [11, 12]]  # Lớp 2
]

# Vector cần tìm lớp
v = [6, 6]

# Tính khoảng cách từ vector v đến các lớp
distances_to_classes = calculate_distances(v, data, distance_metric='euclidean')

print(f'Khoảng cách từ vector v đến các lớp (theo Euclidean): {distances_to_classes}')