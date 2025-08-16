# git_assignment_HeroViredB13
git_assignment_HeroViredB13

CalculatorPlus is a simple Python application that provides basic arithmetic operations and advanced features like square root computation.
This project is built to demonstrate Git workflows, branching strategies, and team collaboration.

✨ Features
Addition
Subtraction
Multiplication
Division (with fix for divide-by-zero error)
Square root (handles negative input errors)

🛠️ Installation & Usage
Clone the repository:
git clone https://github.com/<your-username>/git_assignment_HeroVired.git
cd git_assignment_HeroVired
Run the calculator:
16 + 4 = 20  
16 - 4 = 12  
16 * 4 = 64  
16 / 4 = 4.0  
The square root of 25 = 5.0

📂 Project Structure
text
git_assignment_HeroVired/
│── calculator.py    # Main CalculatorPlus code
│── README.md        # Project documentation
🔀 Git Workflow Implemented
Branches Created
main → Production-ready code
dev → Development branch
feature/sqrt → Square root functionality
lfs → Testing Git LFS
geometry-calculator → Area of circle & rectangle
feature/circle-area → Circle area feature (with Git stash)
feature/rectangle-area → Rectangle area feature (with Git stash)
Version Releases
v1.0 – Initial Calculator app
v2.0 – Added square root + fixed divide-by-zero


📦 Git LFS Integration (for binary files)
This project also demonstrates tracking large files (>200 MB) using Git LFS.

Commands used:
git lfs install
git checkout -b lfs
git lfs track "*.bin"
git add .gitattributes
git add bigfile.bin
git commit -m "Add large binary file with Git LFS"
git push origin lfs

📐 Geometry Calculator 
A separate feature branch contains a GeometryCalculator with:
calculate_circle_area(radius)
calculate_rectangle_area(length, width)
Git Stash Workflow:
Work started on feature/circle-area → stashed changes.
Switched to feature/rectangle-area → stashed changes.
Restored stashes to finish features separately.
Pushed both features & created Pull Requests.

✅ How to Contribute
Fork the repo
Create a branch (feature/new-feature)
Commit your changes
Push the branch and open a Pull Request
🏷️ Version History
v1.0 – Initial release (basic calculator)
v2.0 – Added square root support + divide-by-zero fix

👉 This README gives your classmates (and reviewers) a complete overview of the repo, Git workflow, and features.**
