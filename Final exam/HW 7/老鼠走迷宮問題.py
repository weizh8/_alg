var log = console.log;

// Prints the current state of the maze matrix
function matrixPrint(m) {
  for(var i=0; i<m.length; i++)
    log(m[i]);
}

// Helper: Since JS strings are immutable, this replaces a character at index 'i'
function strset(s, i, c) {
  return s.substr(0, i) + c + s.substr(i+1);
}

function findPath(m, x, y) {
  log("=========================");
  log("Checking coordinates: x=" + x + " y=" + y);
  matrixPrint(m);

  // 1. Boundary Check: Out of bounds?
  if (x >= 6 || y >= 8) return false;
  
  // 2. Obstacle Check: Is it a wall or a known dead end?
  if (m[x][y] == '*' || m[x][y] == '+') return false;

  // 3. Mark the current spot as visited (part of the path)
  if (m[x][y] == ' ') m[x] = strset(m[x], y, '.');

  // 4. Success Condition: Have we reached the edge (the exit)?
  if (m[x][y] == '.' && (x == 5 || y == 7)) 
    return true;

  // 5. Recursive Exploration: Try 4 directions (Right, Down, Left, Up)
  if (y < 7 && m[x][y+1] == ' ') // Move Right
    if (findPath(m, x, y+1)) return true;
    
  if (x < 5 && m[x+1][y] == ' ') // Move Down
    if (findPath(m, x+1, y)) return true;
    
  if (y > 0 && m[x][y-1] == ' ') // Move Left
    if (findPath(m, x, y-1)) return true;
    
  if (x > 0 && m[x-1][y] == ' ') // Move Up
    if (findPath(m, x-1, y)) return true;

  // 6. Backtracking: If no directions work, mark this spot as a dead end (+)
  m[x][y] = strset(m[x], y, '+'); 
  return false;
}

// Define the Maze
var maze = [
  "********", 
  "** * ***",
  "     ***",
  "* ******",
  "* **",
  "***** **"
];

// Start searching from (x=2, y=0)
findPath(maze, 2, 0);
log("======= FINAL RESULT =======");
matrixPrint(maze);
