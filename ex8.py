# assigns variable 'formatter'
formatter = "%r %r %r %r"

# prints formatter with four ints
print formatter % (1, 2, 3, 4)

# prints formatter with four strings
print formatter % ("one", "two", "three", "four")

# prints formatter with four bool commands
print formatter % (True, False, False, True)

# prints formatter with...formatter
print formatter % (formatter, formatter, formatter, formatter)

# prints formatter with four more complex strings
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
