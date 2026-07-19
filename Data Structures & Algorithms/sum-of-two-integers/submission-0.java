class Solution {
    public int getSum(int a, int b) {
        var bitMask = 1;
        var res = 0;
        var carryOver = 0;

        for (var i = 0; i < 32; i++) {
            var bitA = a & bitMask;
            var bitB = b & bitMask;
            res |= bitA ^ bitB ^ carryOver;
            carryOver = bitA & bitB | bitA & carryOver | bitB & carryOver;
            carryOver <<= 1;
            bitMask <<= 1;
        }

        return res;
    }
}
