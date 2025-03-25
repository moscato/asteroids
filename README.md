# Asteroids

This project is still in development.
 <br>
<u>To Fix: <u/>
 <br>
~~Cant close from main.py after re-opening with subprocess~~
  <br>
  ^^ fixed by changing <i>subprocess.run(["python", "main.py"])<i/> to <i>os.execv(sys.executable, main())<i/>
  <br>
Stays running in CLI after closing from game_over.py

![Alt text](asteroids.png)

