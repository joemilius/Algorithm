# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

def largest_altitude(gain)
    altitude = 0
    highest = 0
    for diff in gain
        altitude += diff
        if altitude > highest
            highest = altitude
        end
    end

    highest
    
end

largest_altitude([-5,1,5,0,-7]) # Correct: 1
largest_altitude([-4,-3,-2,-1,4,3,2]) # Correct: 0