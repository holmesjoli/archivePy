import argparse
import textwrap

def parseArguments():
    """
    Command line arguments
    """
    parser = argparse.ArgumentParser(description = 'Arguments for Data Archiving', 
                                        formatter_class = argparse.RawTextHelpFormatter)

    parser.add_argument('-ab', '--add_branch', action = 'store_true', 
                            help = textwrap.dedent('''\
                            Add the branch to the commit tag.
                            (default=%(default)s)
                            ''' ))
    
    parser.add_argument('-am', '--add_message', action = 'store_true', 
                            help = textwrap.dedent('''\
                            Add the message to the commit tag.
                            (default=%(default)s)
                            ''' ))
        
    parser.add_argument('-c', '--commit_message', action = 'store', 
                        help=textwrap.dedent('''\
                        The commit message.
                        (default=%(default)s)
                        '''))


    return vars(parser.parse_args())