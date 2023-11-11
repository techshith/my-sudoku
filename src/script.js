const grid = document.getElementById("sudoku-grid");

function createGrid() {
  for (let row = 0; row < 9; row++) {
    for (let col = 0; col < 9; col++) {
      const input = document.createElement("input");
      input.type = "text";
      input.maxLength = 1;

      input.dataset.row = row;
      input.dataset.col = col;

      input.addEventListener("input", (e) => {
        const value = e.target.value;
        if (!/^[1-9]$/.test(value)) {
          e.target.value = "";
        }
      });

      grid.appendChild(input);
    }
  }
}

createGrid();

function clearBoard() {
    const inputs = grid.querySelectorAll("input");
    inputs.forEach(input => {
      input.value = ""; // clear value
      input.classList.remove("correct", "incorrect"); // remove color classes
      input.style.color = "";       // reset inline styles (optional)
      input.style.borderColor = ""; // reset borders if used
    });
  
    console.log("Board cleared.");
}  