class Connection:
    def __init__(self):
        self.xid = 0

    def _start_transaction(self):
        print("Starting transaction", self.xid)
        rslt = self.xid
        self.xid = self.xid + 1
        return rslt

    def _committransaction(self, xid):
        print('committing transaction', xid)

    def _rollback_transaction(self, xid):
        print('rolling back  transaction', xid)
