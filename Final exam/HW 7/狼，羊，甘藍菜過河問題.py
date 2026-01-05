/**
 * EXERCISE: SOLVING SEARCH PROBLEMS WITH DFS
 * 1. Maze Solver (Mouse in a Maze)
 * 2. River Crossing (Wolf, Goat, and Cabbage)
 */

const log = console.log;

// ==========================================
// PART 1: MAZE SOLVER
// ==========================================
class MazeSolver {
  constructor(maze) {
    this.maze = maze;
    this.rows = maze.length;
    this.cols = maze[0].length;
  }

  // Helper: Since JS strings are immutable, this replaces a character at index 'i'
  strSet(str, index, char) {
    return str.substring(0, index) + char + str.substring(index + 1);
  }

  solve(x, y) {
    // 1. Boundary & Obstacle Check
    if (x < 0 || y < 0 || x >= this.rows || y >= this.cols) return false;
    if (this.maze[x][y] === '*' || this.maze[x][y] === '+') return false;
    
    // 2. Mark current path with a dot '.'
    if (this.maze[x][y] === ' ') {
      this.maze[x] = this.strSet(this.maze[x], y, '.');
    }

    // 3. Check Success: Reached the exit (edge of the maze)
    if (this.maze[x][y] === '.' && (x === this.rows - 1 || y === this.cols - 1)) {
      return true;
    }

    // 4. Recursive Exploration: Try 4 directions (Right, Down, Left, Up)
    const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    for (let [dx, dy] of directions) {
      let nx = x + dx, ny = y + dy;
      // Only proceed if next step is an unvisited path ' '
      if (nx >= 0 && nx < this.rows && ny >= 0 && ny < this.cols && this.maze[nx][ny] === ' ') {
        if (this.solve(nx, ny)) return true;
      }
    }

    // 5. Backtracking: If dead end, mark with '+' and return false
    this.maze[x] = this.strSet(this.maze[x], y, '+');
    return false;
  }

  print() {
    this.maze.forEach(row => log(row));
  }
}

// ==========================================
// PART 2: RIVER CROSSING (WOLF, GOAT, CABBAGE)
// ==========================================
class RiverCrossing {
  constructor() {
    this.objs = ["Human", "Wolf", "Goat", "Cabbage"];
    this.visitedMap = new Set();
    this.path = [];
  }

  // Safety Check: Is anyone being eaten?
  isDead(s) {
    // Wolf eats Goat if Human is on the other side
    if (s[1] === s[2] && s[1] !== s[0]) return true; 
    // Goat eats Cabbage if Human is on the other side
    if (s[2] === s[3] && s[2] !== s[0]) return true; 
    return false;
  }

  // Execute Move: Human moves alone (objIdx 0) or takes one item
  move(s, objIdx) {
    let newS = [...s];
    let nextSide = s[0] === 0 ? 1 : 0;
    newS[0] = nextSide;      // Human changes side
    newS[objIdx] = nextSide; // Object changes side
    return newS;
  }

  solve(s) {
    let sKey = s.join('');
    // Prevent infinite loops by checking visited states
    if (this.visitedMap.has(sKey)) return false;

    this.path.push(s);

    // Success Condition: Everyone has reached side 1
    if (s.every(pos => pos === 1)) {
      log("\n[SUCCESS] River Crossing Sequence:");
      this.path.forEach(p => {
        log(p.map((pos, i) => `${this.objs[i]}${pos}`).join(' '));
      });
      return true;
    }

    this.visitedMap.add(sKey);

    // Identify current side and find available items to transport
    let currentSide = s[0];
    let possibleMoves = [0]; // Human can always cross alone
    for (let i = 1; i < s.length; i++) {
      if (s[i] === currentSide) possibleMoves.push(i);
    }

    // Try all possible legal moves
    for (let objIdx of possibleMoves) {
      let nextState = this.move(s, objIdx);
      if (!this.isDead(nextState)) {
        if (this.solve(nextState)) return true;
      }
    }

    // Backtrack: If this path fails, remove from current path
    this.path.pop(); 
    return false;
  }
}

// --- EXECUTION ---

log("--- SOLVING MAZE PROBLEM ---");
const mazeLayout = [
  "********", 
  "** * ***",
  "     ***",
  "* ******",
  "* **",
  "***** **"
];
const mazeGame = new MazeSolver(mazeLayout);
mazeGame.solve(2, 0); // Start at row 2, col 0
mazeGame.print();

log("\n--- SOLVING RIVER CROSSING PROBLEM ---");
const riverGame = new RiverCrossing();
riverGame.solve([0, 0, 0, 0]); // Start with everyone on side 0
