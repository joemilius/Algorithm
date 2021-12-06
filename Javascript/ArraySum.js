function simpleArraySum(ar) {
    return ar.reduce((previous, current) => previous + current)
}

simpleArraySum([ 1, 2, 3, 4, 10, 11 ])