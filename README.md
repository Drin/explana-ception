# explana-ception
Repository containing code that illustrate and explain various concepts

## Recursion
The recursion materials in this repository all use memo-ized recursion (in
order to be performant, for my own sanity), and are currently based on the
extremely common example of fibonacci numbers.

[Here is a python tutor link illustrating the simple example][simple-recursion-pythontutor]

[Here is a link to a google presentation explaining recursion][recursion-slides]

### Simple
The "simple" recursion example focuses on computing a single fibonacci number,
in order to simplify state that is propagated via the recurrence relation (what
information needs to be returned from the recursive function, and passed as
parameters).

### Advanced
The advanced recursion example passes more complex state via the recurrence
relation, in order to construct the full fibonacci sequence up to the requested
position, and without using a global variable.



[simple-recursion-pythontutor]: https://tinyurl.com/y8nr5ztl
[recursion-slides]: https://docs.google.com/presentation/d/1i0RzAH-SFIdoQdrIjdskeoOTjBv7Jb5FrUfjoXDL0NU/edit?usp=sharing
