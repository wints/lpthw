# define variable 'formatter'
formatter = "%r %r %r %r"

# print formatter with 1-4 integers as variables
print formatter % (1, 2, 3, 4)

# print formatter with one through four as strings
print formatter % ("one", "two", "three", "four")

# print formatter with True and False
print formatter % (True, False, False, True)

# print formatter variable four times
print formatter % (formatter, formatter, formatter, formatter)

# print formatter with the specified stings (a poem!)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)