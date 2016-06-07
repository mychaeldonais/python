from sys import argv
from random import randint
from random import sample
from random import seed

def main( ):

  isAlpha = ( False )
  isNumeric = ( False )
  isUpperCase = ( False )
  isLowerCase = ( False )
  isPunctuation = ( False )

  pwLength = ( 0 )
  numOfOptions = ( 0 )

  try:
    if( len( argv ) > ( 1 ) ):
      for i in range( 0, len( argv ), 1 ):
        if( argv[i] == ( "--alpha" ) ):
          isAlpha = ( True )
        elif( argv[i] == ( "--num" ) ):
          isNumeric = ( True )
        elif( argv[i] == ( "--ucase" ) ):
          isUpperCase = ( True )
        elif( argv[i] == ( "--lcase" ) ):
          isLowerCase = ( True )
        elif( argv[i] == ( "--punc" ) ):
          isPunctuation = ( True )
        elif( argv[i].isnumeric( ) ):
          pwLength = ( int( argv[i] ) )      

      if( pwLength == ( 0 ) ):
        raise ValueError( "Password length should be specified!" )
      elif( pwLength < ( 3 ) ):
        raise ValueError( "Password length should be at least 3 characters!" )
      elif( pwLength >= ( 30 ) ):
        raise ValueError( "Password length should not exceed 30 characters!" ) 
      elif( ( isAlpha and not isUpperCase ) or ( isAlpha and not isLowerCase ) ):
        raise ValueError( "Must specify either uppercase or lowercase letterin!" )
      elif( ( isUpperCase and not isAlpha ) or ( isLowerCase and not isAlpha ) ):
        raise ValueError( "Must specify the alpha switch!" )
    else:
      raise ValueError( "No arguments provided!" )
  except ValueError as e:
    print( "Exception:", e )

  if( isAlpha and isLowerCase ):
    numOfOptions = ( numOfOptions + 1 )

  if( isAlpha and isUpperCase ):
    numOfOptions = ( numOfOptions + 1 )

  if( isNumeric ):
    numOfOptions = ( numOfOptions + 1 )

  if( isPunctuation ):
    numOfOptions = ( numOfOptions + 1 )

  alphaUpperList = ( 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' )

  alphaLowerList = ( 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' )

  numberList = ( '1', '2', '3', '4', '5', '6', '7', '8', '9' )

  puncList = ( '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '`', '~', ',', '<', '.', '>', '/', '?', ';', '\'', '\"', '\\', ':', '[', '{', ']', '}', '|' )

  seed( )

  mainPassword = ( "" )
  tempPassword = ( "" )

  if( isNumeric ):
    for i in range( 0, pwLength, 1 ):
      randVal = ( randint( 0, len( numberList ) - 1 ) )
      tempPassword += ( numberList[randVal] )
  if( isAlpha and isLowerCase ):
    for i in range( 0, pwLength, 1 ):
      randVal = ( randint( 0, len( alphaLowerList ) - 1 ) )
      tempPassword += ( alphaLowerList[randVal] )
  if( isAlpha and isUpperCase ):
    for i in range( 0, pwLength, 1 ):
      randVal = ( randint( 0, len( alphaUpperList ) - 1 ) )
      tempPassword += ( alphaUpperList[randVal] )
  if( isPunctuation ):
    for i in range( 0, pwLength, 1 ):
      randVal = ( randint( 0, len( puncList ) - 1 ) )
      tempPassword += ( puncList[randVal] )

  temp = ( sample( tempPassword , pwLength ) )

  for i in temp:
    mainPassword += ( str( i ) )

  print( "Password:", mainPassword )

if( __name__ == ( "__main__" ) ):
  main( )
