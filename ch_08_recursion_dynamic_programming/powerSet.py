#8.4
set = [1,2,3]
length = len(set)
powers = []
def power_set(set, powers):
    if set not in powers:
        return powers.append(power_set(set[:-1], powers))
    else:
        return powers.append(power_set(set, powers))
    powers.append()
    return powers.append()