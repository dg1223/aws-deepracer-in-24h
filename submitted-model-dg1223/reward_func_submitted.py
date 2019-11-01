def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''
    
    # Give a very low reward by default
    reward = 1e-3
    
    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle']) # Only need the absolute steering angle
    progress = abs(params['progress'])
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    waypoints = params['waypoints']

    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward += 1.0
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    marker_4 = 0.75 * track_width

    # Give higher reward if the agent is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward *= 1
    elif distance_from_center <= marker_2 and distance_from_center > marker_1:
        reward *= 0.8
    elif distance_from_center <= marker_3 and distance_from_center > marker_2:
        reward *= 0.3
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the agent is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.5
        
    # reward for finishing the track
    if progress == 100:
        reward += 1000
    elif progress >= 75 and progress < 100:
        reward += 50
    elif progress >= 50 and progress < 75:
        reward += 5
    elif progress >= 25 and progress < 50:
        reward += 1
    else:
        reward *= 0.9
        
    # penalize for getting too fast around the corners
    if distance_from_center > marker_2 and distance_from_center <= marker_4 and speed > 4:
        reward *= 0.75
    elif distance_from_center > marker_4 and speed > 1:
        reward *= 0.25
        
    # print waypoints for local plotting
    print(*waypoints, sep=',')
    
    return float(reward)