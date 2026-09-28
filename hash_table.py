class HashTable:
    """Hash table implementation using separate chaining."""

    def __init__(self, capacity=4):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        """Compute a deterministic polynomial hash for a string key."""
        hash_value = 0
        base = 31

        for character in str(key):
            hash_value = (
                hash_value * base + ord(character)
            ) % self.capacity

        return hash_value

    def _load_factor(self):
        """Return the current load factor."""
        return self.size / self.capacity

    def insert(self, key, value):
        """Insert a new key-value pair or update an existing key."""
        index = self._hash(key)
        bucket = self.buckets[index]

        # Update the value if the key already exists.
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        # Add the new key-value pair to the chain.
        bucket.append((key, value))
        self.size += 1

        # Resize when the load factor becomes greater than 0.75.
        if self._load_factor() > 0.75:
            self._resize()

    def search(self, key):
        """Return the value associated with a key."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for existing_key, value in bucket:
            if existing_key == key:
                return value

        return None

    def delete(self, key):
        """Delete a key-value pair if the key exists."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                self.size -= 1
                return True

        return False

    def _resize(self):
        """Double the capacity and rehash all existing entries."""
        old_buckets = self.buckets

        self.capacity *= 2
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

        for bucket in old_buckets:
            for key, value in bucket:
                self.insert(key, value)

    def display(self):
        """Display every bucket in the hash table."""
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")


def main():
    table = HashTable(capacity=4)

    print("Inserting key-value pairs...")

    table.insert("Tom", 90)
    table.insert("Jerry", 85)
    table.insert("Cassie", 95)
    table.insert("Rachana", 88)

    print("\nHash table after insertions:")
    table.display()

    print(f"\nCurrent capacity: {table.capacity}")
    print(f"Current load factor: {table._load_factor():.2f}")

    print("\nSearch tests:")
    print("Search Tom:", table.search("Tom"))
    print("Search Cassie:", table.search("Cassie"))
    print("Search Unknown:", table.search("Unknown"))

    print("\nUpdating an existing key:")
    table.insert("Tom", 100)
    print("Updated Tom:", table.search("Tom"))

    print("\nDelete tests:")
    print("Delete Jerry:", table.delete("Jerry"))
    print("Search Jerry after deletion:", table.search("Jerry"))
    print("Delete missing key:", table.delete("Unknown"))

    print("\nFinal hash table:")
    table.display()


if __name__ == "__main__":
    main()