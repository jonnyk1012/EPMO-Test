import sys

def main(talkenid, name):
    print('Execute main Process')
    
    import smartsheet

    # Set a talken ID to get your Smartsheet API access
    print('Talken ID is',talkenid)
    print('Project Name is',name)
    smartsheet = smartsheet.Smartsheet(talkenid)

    # Create folder in "Sheets" folder(Home)
    action = smartsheet.Home.create_folder(name)

    # Set forder Id
    folderId=action.result.id


    # Create sheet in specific folder 
    sheet = smartsheet.models.Sheet({
        'name': 'ProjectSchedule',
        'columns': [{
                'title': 'Favorite',
                'type': 'CHECKBOX',
                'symbol': 'STAR'
            }, {
                'title': 'Primary Column',
                'primary': True,name
                'type': 'TEXT_NUMBER'
            }, {
                'title': 'Status',
                'type': 'PICKLIST',
                'options': [
                    'Not Started',
                    'Started',
                    'Completed'
                ]
            }
        ]
    })

    action = smartsheet.Folders.create_sheet_in_folder(folderId, sheet)
    sheet = action.result

if __name__ = '__main__':
    args = sys.argv
    
    if len(args) == 3:
        talkenid = args[1]
        name     = args[2]
        main(talkenid, name)
    else:
        print('Please specify with following format')
        print('$ create_folder.py <Talken ID> <Project Name>)
        quit()
                  
        
        
        
        
        

