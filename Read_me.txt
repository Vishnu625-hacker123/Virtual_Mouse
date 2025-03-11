# Virtual Mouse

## Overview
The **Virtual Mouse** is an advanced hand gesture-based interface that replaces traditional mouse functions using **computer vision**. This project allows users to move the cursor, click, and scroll seamlessly using hand gestures detected by a webcam.

## Features
- Cursor movement using hand tracking
- Left-click and right-click gestures
- Scroll functionality using finger gestures
- Real-time tracking with OpenCV and MediaPipe
- Enhances accessibility by offering a touch-free interaction experience

## Technologies Used
- **Python**
- **OpenCV** (for real-time video processing)
- **MediaPipe** (for hand tracking)
- **NumPy** (for mathematical operations)

## Installation
To run the project on your local machine, follow these steps:

1. **Clone the repository**
   ```sh
   git clone https://github.com/your-username/virtual-mouse.git
   cd virtual-mouse
   ```

2. **Create a virtual environment (optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Virtual Mouse**
   ```sh
   python virtual_mouse.py
   ```

## Usage
1. Place your hand in front of the webcam.
2. Move your index finger to control the cursor.
3. Tap your index finger and thumb together for a left-click.
4. Tap your middle finger and thumb for a right-click.
5. Move two fingers up or down to scroll.

## Demo
![Virtual Mouse Demo](demo.gif) *(Add a demo GIF or screenshot here)*

## Future Enhancements
- Adding gesture-based drag-and-drop functionality.
- Enhancing accuracy with deep learning-based models.
- Supporting multi-hand gestures for more functionalities.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
**T. Vishnu Vardhan**  
[LinkedIn](https://www.linkedin.com/in/vishnu-vardhan625/)  
[GitHub](https://github.com/your-username)
