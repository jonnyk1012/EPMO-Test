import smartsheet

# Set a talken ID to get your Smartsheet API access
smartsheet = smartsheet.Smartsheet('3xr8utkze73sz8asjygx4td5fl')


# Create folder in "Sheets" folder(Home)
action = smartsheet.Home.create_folder('PMO-test-folder')

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
            'primary': True,
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

print(sheet)

