randomStr = function(e) {
                    for (var t = 0 < arguments.length && void 0 !== e ? e : 10, n = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678", i = n.length, r = "", o = 0; o < t; o++)
                        r += n.charAt(Math.floor(Math.random() * i));
                    return r
                }