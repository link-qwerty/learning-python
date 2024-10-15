# immutable
# ----------------------------------------
immutable_tuple = 1, 2, "string", False
print(immutable_tuple)

#immutable_tuple[0] = 2 -> immutable
#immutable_tuple[3] = True -> immutable too
#immutable_tuple[2] = 'spring' -> aaand... immutable!
#immutable_tuple[2][1] = 'p' what?

# let's try something else
immutable_tuple = 1, 2, ["string"], False
#immutable_tuple[2][0][1] = 'p' -> nope!
immutable_tuple[2][0] = 'spring' # Ok!
print(immutable_tuple)

immutable_tuple = 1, 2, ['s', 't', 'r', 'i', 'n', 'g'], False
#immutable_tuple [2][0][1] = 'p' -> nope!
print(immutable_tuple)

immutable_tuple = 1, 2, [['s', 't', 'r', 'i', 'n', 'g']], False
immutable_tuple [2][0][1] = 'p' # works! but ugly
print(immutable_tuple)

immutable_tuple = 1, 2, [0, 1], False
immutable_tuple[2][0] = 3 #Ok!
immutable_tuple[2][1] = False #Ok!
print(immutable_tuple)

# mutable
# ----------------------------------------
mutable_list = [1, 2, 'string', False]
mutable_list[2] = 'spring'
mutable_list[3] = True
print(mutable_list)