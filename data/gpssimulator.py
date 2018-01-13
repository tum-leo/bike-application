import gpxpy

gpx_file = open('data/radlring-muenchen.gpx', 'r')

gpx = gpxpy.parse(gpx_file)

gpx_file.close()

points = gpx.tracks[0].segments[0].points

current_point = 0


def next_position():
    global current_point
    current_point += 1
    return points[current_point]
