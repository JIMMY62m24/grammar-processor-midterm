# Grammar Processor - Midterm Project

# KABORE TARYAM WILLIAM RODRIGUE  
# CSC 4303  Programming language concepts  
# 7 June 2025

## 📋 Project Description

A Python program that processes context-free grammars and provides two main functionalities:
1. **Word Generation**: Lists all words that a given grammar can produce
2. **Membership Testing**: Determines if a given word belongs to the grammar

## 🚀 Features

- ✅ Interactive command-line interface
- ✅ Support for custom grammar input
- ✅ BFS-based word generation algorithm
- ✅ Reliable membership testing using BFS parsing
- ✅ Built-in example grammar for quick testing
- ✅ Configurable word length and count limits
- ✅ Input validation and error handling

## 📖 Grammar Format

The program accepts grammars in standard BNF notation:
```
S -> aB | bA
A -> a | aS | bAA  
B -> b | bS | aBB
```

Where:
- `S, A, B` are non-terminals (uppercase letters)
- `a, b` are terminals (lowercase letters)
- `|` separates alternative productions
- `->` indicates production rules

## 🎯 Example Usage

### Running the Program
```bash
python grammar_processor.py
```

### Sample Output
```
Grammar Processor
==================================================

Choose input method:
1. Use example grammar
2. Enter custom grammar

Enter choice (1 or 2): 1

Grammar Productions:
====================
A -> a | aS | bAA
B -> b | bS | aBB
S -> aB | bA

Start Symbol: S
Terminals: {a, b}
Non-terminals: {A, B, S}

Generated 50 words:
------------------------------
 1. 'ab'
 2. 'aabb'
 3. 'aab'
 4. 'aabbab'
 ...

Word Membership Testing
==================================================
Enter word to test: ab
✓ 'ab' BELONGS to the grammar

Enter word to test: xyz
✗ 'xyz' does NOT belong to the grammar
```

## 🏗️ Technical Implementation

### Core Algorithms
- **Word Generation**: Breadth-First Search (BFS) expansion of productions
- **Membership Testing**: BFS-based parsing to verify derivation paths
- **Grammar Parsing**: Regular expression-based rule extraction

### Key Classes and Methods
- `GrammarProcessor`: Main class handling all grammar operations
- `parse_grammar()`: Parses input grammar text into internal structures
- `generate_words()`: Uses BFS to generate valid words from grammar
- `belongs_to_grammar()`: Tests if a word can be derived from the grammar

### Data Structures
- `defaultdict`: Stores production rules efficiently
- `deque`: Implements BFS queue for word generation and parsing
- `set`: Tracks visited states to prevent infinite loops

## 📁 Project Structure

```
grammar-processor/
├── grammar_processor.py    # Main program file
├── README.md              # This documentation
└── examples/              # Sample grammar files (optional)
    ├── example1.txt
    └── example2.txt
```

## 🧪 Testing

The program includes built-in testing:
1. Automatically tests generated words to verify correctness
2. Interactive testing interface for custom word validation
3. Input validation for malformed grammars

### Test Cases Covered
- ✅ Valid words from generated set
- ✅ Invalid words with wrong characters
- ✅ Edge cases (empty strings, single characters)
- ✅ Complex multi-step derivations

## 🎓 Educational Objectives Met

1. **Context-Free Grammar Understanding**: Demonstrates parsing and representation
2. **Algorithm Implementation**: BFS for systematic exploration
3. **Data Structure Usage**: Efficient storage and retrieval of grammar rules
4. **User Interface Design**: Clean, interactive command-line experience
5. **Error Handling**: Robust input validation and edge case management

## 💻 Requirements

- **Python 3.7+**
- **Standard Library Only** (no external dependencies)
- **Cross-platform compatibility** (Windows, macOS, Linux)

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/JIMMY62m24/grammar-processor-midterm.git
   cd grammar-processor-midterm
   ```

2. Run the program:
   ```bash
   python grammar_processor.py
   ```

3. Follow the interactive prompts to:
   - Choose example or custom grammar
   - Set generation parameters
   - Test word membership

## 📊 Performance Characteristics

- **Time Complexity**: O(|V|^L) where V is vocabulary size and L is max word length
- **Space Complexity**: O(|G| + |W|) where G is grammar size and W is generated words
- **Optimization**: BFS with visited state tracking prevents exponential blowup

## 🔍 Future Enhancements

- Support for epsilon (ε) productions
- Grammar simplification algorithms
- Graphical user interface
- Export results to file formats
- Grammar equivalence testing

## 📞 Contact

For questions about this implementation, please contact:
- Email: kaboret1@student.iugb.edu.ci
- GitHub:https://github.com/JIMMY62m24/grammar-processor-midterm
---

*This project demonstrates comprehensive understanding of formal language theory, algorithm design, and software engineering principles.*
