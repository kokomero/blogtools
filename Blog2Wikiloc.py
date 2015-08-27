import sys, getopt
import libxml2dom

def usage():
  print ('Usage: ' + sys.argv[0] + ' [-h] -u URL')
  
def print_help():
  usage()
  print ('Get an URL from a Blogger post and print the text content of the post including HTML images.')
  print ('The output of the script can be directly copy-pasted on wikiloc website')
 
def main(argv):
  #Extract arguments
  try:
    opts, args = getopt.getopt(argv, "hu:", ["help", "url="])
  except getopt.GetoptError:
    usage()
    sys.exit(2)

  #Check we got some arguments
  if len( opts ) == 0:
    usage()
    sys.exit(2)

  #Parse command line arguments
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      print_help()
      sys.exit()
    elif opt in ("-u", "--url"):
      url = arg

  #Open the HTML documment from blogger
  document = libxml2dom.parse(url, html=1)

  #Create the XPath expression to look for the entry content
  xpression = "//div[@class='post-body entry-content']//span"
  nodes = document.xpath( xpression )
  
  #First print a href link to the blog post
  print '<a href="' + url + '"> Link to the blog post - Enlace a la pagina en el blog</a>'
  
  #For each node in the post content, check whether it is an img or plain textContent
  for i in nodes:
    #If img node
    if ( len( i.getElementsByTagName("img") ) > 0):
      print (i.getElementsByTagName("img")[0].toString())
      print ("<br />")
    else:
      print (i.textContent)

  #Exit
  sys.exit()

if __name__ == "__main__":
  main(sys.argv[1:])
