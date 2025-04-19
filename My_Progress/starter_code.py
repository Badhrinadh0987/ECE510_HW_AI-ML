from scipy.spatial import distance as dist

def calculate_ear(eye):
    # vertical distances
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    # horizontal distance
    C = dist.euclidean(eye[0], eye[3])
    # EAR calculation
    ear = (A + B) / (2.0 * C)
    return ear