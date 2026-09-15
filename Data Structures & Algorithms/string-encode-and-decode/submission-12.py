class Solution:
    def encode(self, strs):
        # Efficient string concatenation
        encoded_parts = []
        lengths = []

        for word in strs:
            encoded_parts.append(word)
            lengths.append(str(len(word)))

        # Only one trailing delimiter, no extras
        return ''.join(encoded_parts) + "YUBI" + "YUBI".join(lengths)

    def decode(self, s):
        parts = s.split("YUBI")

        # Last part might be empty if there's a trailing delimiter
        if parts[-1] == "":
            parts.pop()

        # First part is the concatenated encoded string
        encoded = parts[0]

        # The rest are lengths
        lengths = list(map(int, parts[1:]))

        res = []
        i = 0
        for length in lengths:
            res.append(encoded[i:i + length])
            i += length

        return res
