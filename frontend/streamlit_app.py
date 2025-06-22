import streamlit as st
import requests

st.set_page_config(page_title="RAG Maritime Incident App", layout="wide")
st.title("🚢 Maritime Incident Summarizer (RAG-based)")

st.markdown("Click **Summarize** to run the RAG pipeline using FastAPI backend.")

if st.button("🔍 Summarize Incidents"):

    incident_text =  [
    {
        'event': 'Fire in engine room',
        'eventdate': '12-07-2023',
        'longdesc': 'A fire broke out in the engine room due to overheating of machinery.',
        'veseltype': 'Tanker',
        'rootcause': 'Lack of maintenance'
    },
    {
        'event': 'Oil spill during loading',
        'eventdate': '15-08-2023',
        'longdesc': 'Oil spill occurred while loading cargo due to hose failure.',
        'veseltype': 'Tanker',
        'rootcause': 'Equipment failure'
    },
    {
        'event': 'Crew injury on deck',
        'eventdate': '21-09-2023',
        'longdesc': 'A crew member slipped and fell during mooring operations.',
        'veseltype': 'Tanker',
        'rootcause': 'Wet surface and poor footwear'
    },
    {
        'event': 'Navigation equipment failure',
        'eventdate': '02-10-2023',
        'longdesc': 'Radar and GPS malfunctioned while sailing in restricted waters.',
        'veseltype': 'Tanker',
        'rootcause': 'Electrical issue'
    },
    {
        'event': 'Collision with berth',
        'eventdate': '18-11-2023',
        'longdesc': 'The vessel hit the berth while maneuvering due to strong currents.',
        'veseltype': 'Tanker',
        'rootcause': 'Improper speed control'
    },
    {
        'event': 'Engine breakdown',
        'eventdate': '30-11-2023',
        'longdesc': 'Main engine stopped suddenly while transiting open sea.',
        'veseltype': 'Tanker',
        'rootcause': 'Lubrication failure'
    },
    {
        'event': 'Anchor dragging',
        'eventdate': '12-12-2023',
        'longdesc': 'Vessel dragged anchor during rough weather, nearly grounding.',
        'veseltype': 'Tanker',
        'rootcause': 'Improper anchoring'
    },
    {
        'event': 'Cargo contamination',
        'eventdate': '03-01-2024',
        'longdesc': 'Mixed cargo tanks led to contamination of refined oil.',
        'veseltype': 'Tanker',
        'rootcause': 'Valve misoperation'
    },
    {
        'event': 'Fire alarm false trigger',
        'eventdate': '07-01-2024',
        'longdesc': 'Frequent false fire alarms disrupted crew activities.',
        'veseltype': 'Tanker',
        'rootcause': 'Sensor malfunction'
    },
    {
        'event': 'Crew member illness',
        'eventdate': '20-01-2024',
        'longdesc': 'A crew member showed signs of appendicitis and required evacuation.',
        'veseltype': 'Tanker',
        'rootcause': 'Medical emergency'
    },
    {
        'event': 'Leak in ballast tank',
        'eventdate': '28-01-2024',
        'longdesc': 'Discovered sea water leakage in ballast tank during routine inspection.',
        'veseltype': 'Tanker',
        'rootcause': 'Corrosion'
    },
    {
        'event': 'Blackout at sea',
        'eventdate': '03-02-2024',
        'longdesc': 'Complete loss of electrical power for 10 minutes.',
        'veseltype': 'Tanker',
        'rootcause': 'Generator failure'
    },
    {
        'event': 'Man overboard drill failed',
        'eventdate': '09-02-2024',
        'longdesc': 'Crew did not respond timely during a planned MOB drill.',
        'veseltype': 'Tanker',
        'rootcause': 'Poor training'
    },
    {
        'event': 'Breach of security',
        'eventdate': '15-02-2024',
        'longdesc': 'Unauthorized personnel boarded at anchorage.',
        'veseltype': 'Tanker',
        'rootcause': 'Inadequate watchkeeping'
    },
    {
        'event': 'Improper tank cleaning',
        'eventdate': '21-02-2024',
        'longdesc': 'Cargo residue remained due to poor tank cleaning procedure.',
        'veseltype': 'Tanker',
        'rootcause': 'Incorrect procedures'
    },
    {
        'event': 'Hydraulic system leak',
        'eventdate': '25-02-2024',
        'longdesc': 'Hydraulic oil leaked near steering gear.',
        'veseltype': 'Tanker',
        'rootcause': 'Worn-out seals'
    },
    {
        'event': 'High sulfur fuel used mistakenly',
        'eventdate': '28-02-2024',
        'longdesc': 'Bunker fuel had higher sulfur content than regulations allow.',
        'veseltype': 'Tanker',
        'rootcause': 'Bunker supply error'
    },
    {
        'event': 'Rough weather damage',
        'eventdate': '03-03-2024',
        'longdesc': 'Deck fittings damaged due to extreme swell.',
        'veseltype': 'Tanker',
        'rootcause': 'Improper lashing'
    },
    {
        'event': 'Poor visibility navigation error',
        'eventdate': '09-03-2024',
        'longdesc': 'Wrong turn taken due to poor radar watch during fog.',
        'veseltype': 'Tanker',
        'rootcause': 'Negligent lookout'
    },
    {
        'event': 'Fuel line rupture',
        'eventdate': '12-03-2024',
        'longdesc': 'Main engine fuel line ruptured causing minor fire.',
        'veseltype': 'Tanker',
        'rootcause': 'Old pipeline'
    },
    {
        'event': 'Improper cargo documentation',
        'eventdate': '15-03-2024',
        'longdesc': 'Cargo manifest did not match actual loaded quantity.',
        'veseltype': 'Tanker',
        'rootcause': 'Clerical error'
    },
    {
        'event': 'Gangway collapsed',
        'eventdate': '18-03-2024',
        'longdesc': 'Portable gangway collapsed during boarding.',
        'veseltype': 'Tanker',
        'rootcause': 'Faulty installation'
    },
    {
        'event': 'Unplanned drydock entry',
        'eventdate': '20-03-2024',
        'longdesc': 'Emergency drydock needed due to hull damage.',
        'veseltype': 'Tanker',
        'rootcause': 'Unknown underwater contact'
    },
    {
        'event': 'Fire drill performance unsatisfactory',
        'eventdate': '25-03-2024',
        'longdesc': 'Crew response time during fire drill exceeded allowable time.',
        'veseltype': 'Tanker',
        'rootcause': 'Lack of preparedness'
    },
    {
        'event': 'Spillage during bunkering',
        'eventdate': '28-03-2024',
        'longdesc': 'Fuel spilled on deck due to overflow.',
        'veseltype': 'Tanker',
        'rootcause': 'No communication between teams'
    },
    {
        'event': 'Navigation error at pilot boarding area',
        'eventdate': '01-04-2024',
        'longdesc': 'Approached wrong pilot station due to miscommunication.',
        'veseltype': 'Tanker',
        'rootcause': 'Chart misreading'
    },
    {
        'event': 'Mooring rope snapped',
        'eventdate': '04-04-2024',
        'longdesc': 'A mooring line snapped while vessel was alongside berth.',
        'veseltype': 'Tanker',
        'rootcause': 'Overtension'
    },
    {
        'event': 'Steering gear failure',
        'eventdate': '08-04-2024',
        'longdesc': 'Steering became unresponsive while vessel was in channel.',
        'veseltype': 'Tanker',
        'rootcause': 'Hydraulic issue'
    },
    {
        'event': 'Unsafe ladder rigging',
        'eventdate': '12-04-2024',
        'longdesc': 'Pilot ladder not rigged as per standard, delaying pilot boarding.',
        'veseltype': 'Tanker',
        'rootcause': 'Negligence'
    },
    {
        'event': 'Hull breach by floating object',
        'eventdate': '15-04-2024',
        'longdesc': 'Floating container struck the hull causing a dent below waterline.',
        'veseltype': 'Tanker',
        'rootcause': 'Watch failure'
    }
    ]



    with st.spinner("Sending data to FastAPI backend..."):
        res = requests.post("http://localhost:8000/generate_report",json={"incidents": incident_text})
        # print(res.json())
        # print(res.status_code, res.text)

    if res.status_code == 200:
        result = res.json()
        st.markdown("### Incident Summary")
        st.code(result.get("incident_summary", "Not found"))

        st.markdown("### Retrieved SOP Context")
        st.code(result.get("sop_context", "Not found"))

        st.markdown("### Final Report")
        st.markdown(result.get("report", "Not found"))
    else:
        st.error("Failed to fetch report from backend.")
