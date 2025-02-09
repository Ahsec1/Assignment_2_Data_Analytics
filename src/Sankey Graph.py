import plotly.graph_objects as go

labels = [
    'PS', 'OMP', 'CNP', 'NRP', 'NMCCC', 'PEC', 'NCDM', 'RGS',  
    'S', 'I', 'D', 'F', 'N',  
    'Reg', 'Aca', 'Oth'  
]

sources = [
    0, 0, 1, 2, 3, 4, 5, 6, 7,  
    1, 2, 4, 5, 6,
    
    8, 9, 10, 11, 12  
]

targets = [
    8, 9, 10, 11, 12, 8, 9, 10, 11,  
    10, 11, 12, 8, 9,

    13, 14, 14, 15, 13  
]

values = [
    5, 3, 4, 2, 3, 5, 1, 4, 2,  
    3, 2, 1, 4, 3,

    4, 3, 5, 2, 6  
]

fig = go.Figure(go.Sankey(
    node=dict(
        pad=20,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=["#FFA07A", "#20B2AA", "#9370DB", "#FFD700", "#FF69B4", "#8FBC8F", "#00CED1", "#FFA500", 
               "#1E90FF", "#98FB98", "#D2691E", "#FF4500", "#800080",  
               "#4682B4", "#32CD32", "#B22222"],
        x=[
            0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,  
            0.5, 0.5, 0.5, 0.5, 0.5,  
            0.9, 0.9, 0.9  
        ],
        y=[
            0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,  
            0.2, 0.4, 0.6, 0.3, 0.7,  
            0.2, 0.5, 0.8  
        ]
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color=[
            "rgba(255,99,71,0.7)", "rgba(135,206,250,0.7)", "rgba(221,160,221,0.7)", "rgba(255,215,0,0.7)", 
            "rgba(255,182,193,0.7)", "rgba(144,238,144,0.7)", "rgba(32,178,170,0.7)", "rgba(255,140,0,0.7)", 
            "rgba(30,144,255,0.7)", "rgba(72,209,204,0.7)", "rgba(244,164,96,0.7)", "rgba(147,112,219,0.7)", 
            "rgba(210,105,30,0.7)", "rgba(250,128,114,0.7)", "rgba(255,0,0,0.7)", "rgba(0,0,255,0.7)", 
            "rgba(0,255,0,0.7)", "rgba(255,165,0,0.7)", "rgba(128,0,128,0.7)"
        ]
    )
))

fig.update_layout(
    title_text="Sankey Diagram: Sources → Middle Set → Targets",
    font_size=12
)

fig.show()
