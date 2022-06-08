def rename_duplicate_shape_names(pres_path, overwrite=True):
    ''' 
    Ensures all shapes have a unique name. 
    Only renames duplicates. 
    Compares shape names one slide at a time. 
    '''

    file_name = basename(pres_path).split('.')[0]
    file_path = dirname(pres_path)

    prs = Presentation(pres_path)

    for slide in prs.slides:
        shape_names = []
        for shape in slide.shapes:
            shape_names.append(shape.name)
        renamed_shapes = [x + "_" + str(i) if shape_names.count(x)>1 else x for i, x in enumerate(shape_names)]
        for s_idx, shape in enumerate(slide.shapes):
            shape.name = renamed_shapes[s_idx]

    if overwrite:
        prs.save('{pres_path}\\{pres_name}.pptx'.format(
            pres_path=file_path, 
            pres_name=file_name))
    else:
        prs.save('{pres_path}\\{pres_name}_edited.pptx'.format(
            pres_path=file_path, 
            pres_name=file_name)) 
        
        def get_chart_data_from_prs(pres_path, slide_num, chart_name):
    '''
    This function 1) pulls a given chart's data and 2) returns it as a pandas dataframe object in a list
    
    param: pres_path - full path of target file
    param: slide_num - takes a list of slides 
    param: chart_name - object name as it appears within powerpoint's Object Selection Pane
    '''
    
    prs = Presentation(pres_path)
    
    collection_of_dfs = []

    for i, sld in enumerate(prs.slides, start=1):
        if i in slide_num: 
            for x, shp in enumerate(sld.shapes):
                
                if shp.name == chart_name:
                    
                    plot = shp.chart.plots[0]

                    columns = []
                    data = []
                    for series in plot.series:
                        columns.append(str(series.name))
                        data.append(series.values)
                  
                    data = np.array(data)
                    rows = np.array(plot.categories)
                      
                    df = pd.DataFrame(data.T, index=rows, columns=columns)    
                    collection_of_dfs.append(df)

    return(collection_of_dfs) 
