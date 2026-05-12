cat <<EOF > smart_bug_bounty/bug_descriptions.md
# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return the last n items in a list.
- **Current Issue**: Off-by-one error due to an incorrect start index in the slice.

## bug2.js
- **Intended Behavior**: Sum all numeric values in an array.
- **Current Issue**: Loop boundary error (\`i <= length\`) causes addition of an undefined element.

## bug3.java
- **Intended Behavior**: Return the precise average of an integer array as a double.
- **Current Issue**: Integer division occurs because both operands are integers, losing precision.

## bug4.py
- **Intended Behavior**: Add an item to a list that defaults to empty on every fresh call.
- **Current Issue**: Uses a mutable default argument which persists state between calls.
EOF
