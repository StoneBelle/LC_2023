/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    
    return function() {
        // Variable to store initial value of n
        m = n
        
        // Return the initial n value the first time function is called
        if (n === m){
            n += 1
            return m
        // Increment n by 1 after the first function call
        } else {
            return n += 1
        }
        

    };
};

