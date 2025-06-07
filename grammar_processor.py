import re
from collections import defaultdict, deque
from typing import Dict, List, Set, Tuple, Optional
import itertools

class GrammarProcessor:
    def __init__(self):
        self.productions = defaultdict(list)  # Non-terminal -> list of productions
        self.terminals = set()
        self.non_terminals = set()
        self.start_symbol = None
        
    def parse_grammar(self, grammar_text: str) -> None:
        """
        Parse grammar from text format.
        Expected format:
        S -> aB | bA
        A -> a | aS | bAA
        B -> b | bS | aBB
        """
        lines = [line.strip() for line in grammar_text.strip().split('\n') if line.strip()]
        
        for line in lines:
            if '->' not in line:
                continue
                
            left, right = line.split('->', 1)
            left = left.strip()
            
            # Set start symbol as the first non-terminal encountered
            if self.start_symbol is None:
                self.start_symbol = left
            
            self.non_terminals.add(left)
            
            # Split productions by '|'
            productions = [prod.strip() for prod in right.split('|')]
            
            for prod in productions:
                self.productions[left].append(prod)
                
                # Extract terminals and non-terminals from production
                for char in prod:
                    if char.isupper():
                        self.non_terminals.add(char)
                    elif char.islower():
                        self.terminals.add(char)
    
    def generate_words(self, max_length: int = 10, max_words: int = 100) -> List[str]:
        """
        Generate words that the grammar can produce using BFS approach.
        """
        if not self.start_symbol:
            return []
        
        generated_words = set()
        queue = deque([self.start_symbol])
        visited_strings = set([self.start_symbol])
        
        while queue and len(generated_words) < max_words:
            current = queue.popleft()
            
            # If current string contains only terminals, it's a word
            if self._is_terminal_string(current):
                if len(current) <= max_length and current:
                    generated_words.add(current)
                continue
            
            # If string is too long, skip it
            if len(current) > max_length:
                continue
            
            # Find all possible expansions
            expansions = self._get_expansions(current)
            
            for expansion in expansions:
                if expansion not in visited_strings and len(expansion) <= max_length * 2:
                    visited_strings.add(expansion)
                    queue.append(expansion)
        
        return sorted(list(generated_words))
    
    def _is_terminal_string(self, s: str) -> bool:
        """Check if string contains only terminal symbols."""
        return all(char in self.terminals or char == '' for char in s)
    
    def _get_expansions(self, current: str) -> List[str]:
        """Get all possible one-step expansions of current string."""
        expansions = []
        
        # Find first non-terminal and expand it
        for i, char in enumerate(current):
            if char in self.non_terminals:
                for production in self.productions[char]:
                    # Replace the non-terminal with the production
                    new_string = current[:i] + production + current[i+1:]
                    expansions.append(new_string)
                break  # Only expand the first non-terminal found
        
        return expansions
    
    def belongs_to_grammar(self, word: str) -> bool:
        """
        Check if a word belongs to the grammar using improved parsing.
        """
        if not word:
            return self._can_produce_empty()
        
        # Check if word contains only valid terminals
        if not all(char in self.terminals for char in word):
            return False
        
        # Use BFS to check if word can be generated
        return self._bfs_parse(word)
    
    def _can_produce_empty(self) -> bool:
        """Check if grammar can produce empty string."""
        # Simple check: see if any production leads to empty string
        queue = deque([self.start_symbol])
        visited = set([self.start_symbol])
        
        while queue:
            current = queue.popleft()
            
            if current == '':
                return True
            
            if self._is_terminal_string(current):
                continue
            
            expansions = self._get_expansions(current)
            for exp in expansions:
                if exp not in visited and len(exp) < 20:  # Prevent infinite loops
                    visited.add(exp)
                    queue.append(exp)
        
        return False
    
    def _bfs_parse(self, target_word: str) -> bool:
        """
        Use BFS to check if target word can be generated from start symbol.
        """
        if not self.start_symbol:
            return False
        
        queue = deque([self.start_symbol])
        visited = set([self.start_symbol])
        max_iterations = 10000  # Prevent infinite loops
        iterations = 0
        
        while queue and iterations < max_iterations:
            iterations += 1
            current = queue.popleft()
            
            # If we found the target word, return True
            if current == target_word:
                return True
            
            # If current string is terminal but not our target, skip
            if self._is_terminal_string(current):
                continue
            
            # If current string is longer than target, skip
            if len(current) > len(target_word):
                continue
            
            # Get all possible expansions
            expansions = self._get_expansions(current)
            
            for expansion in expansions:
                if expansion not in visited:
                    visited.add(expansion)
                    queue.append(expansion)
        
        return False
    
    def display_grammar(self) -> str:
        """Display the parsed grammar in a readable format."""
        result = "Grammar Productions:\n"
        result += "=" * 20 + "\n"
        
        for nt in sorted(self.non_terminals):
            if nt in self.productions:
                productions = " | ".join(self.productions[nt])
                result += f"{nt} -> {productions}\n"
        
        result += f"\nStart Symbol: {self.start_symbol}\n"
        result += f"Terminals: {{{', '.join(sorted(self.terminals))}}}\n"
        result += f"Non-terminals: {{{', '.join(sorted(self.non_terminals))}}}\n"
        
        return result

def main():
    """Main function to demonstrate the grammar processor."""
    processor = GrammarProcessor()
    
    print("Grammar Processor")
    print("=" * 50)
    print("\nChoose input method:")
    print("1. Use example grammar")
    print("2. Enter custom grammar")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == "1":
        # Example grammar
        example_grammar = """
        S -> aB | bA
        A -> a | aS | bAA
        B -> b | bS | aBB
        """
        processor.parse_grammar(example_grammar)
        print("\nUsing example grammar:")
        print(example_grammar)
    
    elif choice == "2":
        print("\nEnter grammar (one production per line, empty line to finish):")
        print("Format: S -> aB | bA")
        
        grammar_lines = []
        while True:
            line = input().strip()
            if not line:
                break
            grammar_lines.append(line)
        
        if grammar_lines:
            processor.parse_grammar('\n'.join(grammar_lines))
        else:
            print("No grammar entered. Using example grammar.")
            example_grammar = """
            S -> aB | bA
            A -> a | aS | bAA
            B -> b | bS | aBB
            """
            processor.parse_grammar(example_grammar)
    
    else:
        print("Invalid choice. Using example grammar.")
        example_grammar = """
        S -> aB | bA
        A -> a | aS | bAA
        B -> b | bS | aBB
        """
        processor.parse_grammar(example_grammar)
    
    # Display parsed grammar
    print("\n" + processor.display_grammar())
    
    # Generate words
    print("\nGenerating words from grammar...")
    max_length = int(input("Enter maximum word length (default 8): ") or "8")
    max_words = int(input("Enter maximum number of words (default 50): ") or "50")
    
    words = processor.generate_words(max_length, max_words)
    
    print(f"\nGenerated {len(words)} words:")
    print("-" * 30)
    for i, word in enumerate(words, 1):
        print(f"{i:2d}. '{word}'")
    
    # Test word membership
    print("\n" + "=" * 50)
    print("Word Membership Testing")
    print("=" * 50)
    
    # First, test some generated words to verify the algorithm works
    print("\nTesting some generated words first:")
    test_samples = words[:5] if len(words) >= 5 else words
    for word in test_samples:
        belongs = processor.belongs_to_grammar(word)
        status = "✓ BELONGS" if belongs else "✗ does NOT belong"
        print(f"'{word}' {status} to the grammar")
    
    print("\nNow test your own words:")
    while True:
        test_word = input("\nEnter word to test (or 'quit' to exit): ").strip()
        
        if test_word.lower() == 'quit':
            break
        
        if processor.belongs_to_grammar(test_word):
            print(f"✓ '{test_word}' BELONGS to the grammar")
        else:
            print(f"✗ '{test_word}' does NOT belong to the grammar")
    
    print("\nThank you for using Grammar Processor!")

if __name__ == "__main__":
    main()
