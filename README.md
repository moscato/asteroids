# asteroids

This project is still in development.
 <br>
<u>To Fix<u/>
 <br>
~~Cant close from main.py after re-opening with subprocess~~
  <br>
  ^^ fixed by changing subprocess.run(["python", "main.py"]) to os.execv(sys.executable, main())
  <br>
Stays running in CLI after closing from game_over.py
