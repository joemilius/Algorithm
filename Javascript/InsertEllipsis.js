function truncateString(str, num) {
    let truncate = []
    let joined = ''
    if(str.length > num){
      truncate.push(str.substring(0, num))
      truncate.push('...')
      joined = truncate.join('')
    }
    console.log(joined)
    return joined;
  }
  
  truncateString("A-tisket a-tasket A green and yellow basket", 8);