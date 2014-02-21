# $HeadURL$
__RCSID__ = "ffae789 (2011-03-18 13:12:27 +0000) Ricardo Graciani <graciani@ecm.ub.es>"

class MappingTable:

  #############################################################################
  def __init__( self ):
    """ MappingTable constructor
    """
    self.tableData = list()
    self.columns = list()

  #############################################################################  
  def __del__( self ):
    """ MappingTable destructor
    """
    pass

  #############################################################################  
  def newTable( self ):
    """ Create a new table
    """
    self.tableData = ''

  #############################################################################  
  def setColumns( self, names ):
    """ Set the column names (pass a list of names)
    """
    self.columns = names

  #############################################################################  
  def addRow( self, data ):
    """ Adds a new row to the table (pass a list of data)
    """
    self.tableData.append( data )

  #############################################################################
  def tableToHTML( self ):
    """ Outputs the data as HTML. (Make sure to link to myTable.css)
    """
    output = ''
    output += '<div class="myTable">'

    output += '<div class="myTableHeader">'
    output += '<ul>'
    for col in self.columns:
      output += '<li>%s</li>' % col
    output += '</ul>'
    output += '</div>'

    for row in range( 0, len( self.tableData ) ):
      output += '<div class="myTableRow%d">' % ( ( row % 2 ) + 1 )
      output += '<ul>'
      for col in self.tableData[row]:
        output += '<li>%s</li>' % col
      output += '</ul>'
      output += '</div>'

    output += '</div>'

    return output
