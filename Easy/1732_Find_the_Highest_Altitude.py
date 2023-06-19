class Solution(object):
    def largestAltitude(self, gain):
        
        # Altitude starts at 0
        alt = 0 
        all_alts = [0]

        # Iterate through gain, adding gain[i] to current alt
        for g in gain:
            alt += g
            all_alts.append(alt)

        # Return the highest altitude
        return max(all_alts)
