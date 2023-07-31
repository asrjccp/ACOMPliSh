import streamlit as st
from relationaldatabase import ask_GPT
from langchain.prompts import PromptTemplate
from PIL import Image
st.set_page_config(
    page_title = "Relational Database",
    page_icon = "💻",
)
st.title('💻 Relational Database GPT')
st.caption("Click on the buttons for all the info!")
# Template
question_template = PromptTemplate(
    input_variables=['topic'],
    template=''' You are a H2 Computing Tutor in Singapore and you are teaching relational databases.
    Your role is to give a summary on {topic} and make sure its only relevant to {topic}'''
)

# Put Buttons together in Columns
col1, col2, col3 = st.columns(3)
# In Column 1
with col1:
    rd_definitions = st.button("Definitions")
if rd_definitions:
    st.markdown("**primary key:** Atoms of an element that have the **:red[same number of protons]** but **:red[different number of neutrons]**")
    #st.markdown("**foreign key**: The electrons in an atom are arranged in electronic shell")
    st.markdown("**1NF (First Normal Form)**: **no** **:red[repeating fields/groups]**")
    st.markdown("**2NF (Second Normal Form)**: **no **:red[partial key]** dependency**.")
    st.markdown("**3NF (Third Normal Form)**: **no **:red[non-key]** dependency**.")

# In Column 2
with col2:
    ie = st.button("Ionisation Energy Factors")
if ie:
    st.markdown("**:blue[1. Nuclear Charge]**")
    st.markdown(
    """
    - As the number of proton increases, the nuclear charge :red[increases]
    - The attraction of the positively charged nucleus for the negatively charged valence electrons :red[becomes stronger]. 
    - :red[More] energy is required to remove the valence electrons.
    - Hence, the ionisation energy :red[increases].
    """
    )
    st.markdown("**:blue[2. Shielding Effect by other electrons]**")
    shield_effect_img = Image.open("./pages/Images/ShieldingEffect.png")
    st.image(shield_effect_img)
    st.markdown(
    """
    - Shielding effect increases with an :red[increase] in the number of inner electronic shells
    - Thus, the electrostatic attractions between the valence electron and the nuclues :red[becomes weaker]
    - :red[Less energy] is required to remove the valence electron
    - Ionisation Energy :red[Decreases]
    """
    )
    st.markdown("**:blue[3. No. of electronic shells (distance)]**")
    st.markdown(
    """
    - As the number of electrons shells increases, the valence electrons are :red[further away] and :red[more shielded] from the nucleus
    - The attraction of the positively charged nucleus and the negatively charged electrons :red[becomes weaker]
    - :red[Less energy] is required to remove the valence electrons
    - Ionisation energy :red[decreases]
    """
    )


# Column 3
with col3:
    as_trends = st.button("I.E. Trends")
if as_trends:
    as_trend_img = Image.open("./pages/Images/IETrend.png")
    st.image(as_trend_img)
    st.markdown("**:blue[Across a Period:]**")
    st.markdown(
    """
    - Across a period, number of protons increases and hence :red[nuclear charge increases].
    - Across a period, :red[number of electrons also increases] but these electrons are added to the same outermost electron shell and hence number of electron shells remains the same and :red[shielding effect remains approximately constant]
    - Electrostatic :red[attraction] between the valence electrons and the nucleus :red[becomes stronger].
    - Hence :red[more energy] is required to remove a valence electron from an atom across a period.
    - First ionisation energies :red[generally increase] across a period.

    """
    )
    st.markdown("**:blue[Group 2 & 13 Anomaly:]**")
    st.markdown(
    """
    Mg: 1s2 2s2 2p6 **3s2**
    
    Al: 1s2 2s2 2p6 3s2 **3p1**

    - Nuclear charge of Al is higher than Mg.
    - However, the 3p electron to be removed from Al is at a :red[higher energy level] and :red[less strongly attracted to the nucleus] than the 3s electron to be removed from Mg.
    - Hence :red[less energy] is required to remove the 3p electron in Al than the 3s electron in Mg.
    - Consequently the first ionisation energy of Al is :red[lower] than that of Mg.

    """)
    st.markdown("**:blue[Group 15 & 16 Anomaly:]**")
    st.markdown(
    """
    N : 1s2 2s2 **2p3**

    O : 1s2 2s2 **2p4**

    - Nuclear charge of O is higher than N.
    - However, the 2p electron to be removed from O is a :red[paired electron] while that to be removed from N is an :red[unpaired electron]. 
    - Due to :red[inter–electronic repulsion] between paired electrons in the same orbital, :red[less energy] is required to remove the 2p electron from O.
    - Hence the first ionisation energy of O is :red[lower] than that of N.
    """
    )
    st.markdown("**:blue[Down the Group:]**")
    st.markdown(
    """
    - Nuclear charge increases
    - However, the :red[number of electron shells increase], which result in :red[valence electron further away and is more shielded] from the nucleus
    - Electrostatic :red[attraction] between the valence electron and the nucleus :red[becomes weaker]
    - :red[Less energy] is required for the removal of valence electron
    - First I.E. of elements :red[generally decrease] down a group.

    """)
col4, col5, col6 = st.columns(3)
# Column 4
with col4:
    angle_of_deflection = st.button("Angle of Deflection")
if angle_of_deflection:
    as_angle_of_deflection = Image.open("./pages/Images/AngleofDeflection.png")
    st.image(as_angle_of_deflection)
    st.latex(r'''Angle of Deflection, \theta = \frac{q}{m}''')
    st.markdown(
    """
    - Angle of Deflection, θ, is proportional to the **:red[charge]** of the particle, but **:red[inversely proportional]** to its mass
    - Particles with **:red[smaller mass]** and/or **:red[higher charge]** will be deflected more.
    - The greater the charge of the particle, the greater is the attractive force exerted on it from the oppositely charged plate, and the greater is the deviation from its original direction of motion
    - If two particles are moving at the same speed but one is more massive than the other, the heavier particle has a greater kinetic energy. Thus, more energy must be exerted on the heavier particle to cause it to deflect. Since the applied electric field is exerting the same amount of force on these two different particles with different masses, the **:red[heavier particle is deflected to a lesser extent]**

    """
    )

# Column 5
with col5:
    as_orbitals = st.button("Orbitals")
if as_orbitals:
    st.markdown("**:blue[Orbitals:]**")
    st.markdown(
    """
    - Electrons are not “fixed” in place; rather they are spread out around the nucleus as an electron cloud known as **:red[orbital]**.
    - An orbital represents a three–dimensional volume of space around the nucleus in which there is a **:red[high probability (> 95%) of finding an electron]**.
    """
    )
    st.markdown("**:blue[Shape of Orbitals]**")
    st.markdown("**s orbitals**")
    st.markdown(
    """
    - The s orbital is **:red[spherically symmetrical]** about the nucleus.
    - The probability of finding an electron at a distance r from the nucleus is the same in all directions.
    - An s orbital is represented by drawing a circle.
    - s orbitals from different principal electronic shells **:red[differ in size]**.
    """
    )
    as_s_orbitals = Image.open("./pages/Images/sOrbitals.png")
    st.image(as_s_orbitals)
    st.markdown("**p orbitals**")
    st.markdown(
    """
    - A p subshell is made up of three **:red[dumb–bell]** shaped p orbitals mutually at **:red[right angles]** to each other. 
    - Each p orbital consists of two lobes with the atomic nucleus lying between them.
    - p orbitals are **:red[directional]**, e.g. the px orbital will have 2 lobes of high electron density that lie along the x axis. 
    - All the three p orbitals are **:red[degenerate]**, i.e. they have the **:red[same energy]**. 
    - p orbitals from different electronic shell shells **:red[differ in size.]** Like s orbitals, the p orbitals get larger and more diffused as the principal quantum number, n, increases. i.e. 3p > 2p
    """
    )
    as_p_orbitals = Image.open("./pages/Images/pOrbitals.png")
    st.image(as_p_orbitals)
    st.markdown("**d orbitals**")
    st.markdown(
    """
    - A d subshell consists of 5 orbitals which are **:red[degenerate]** (dxy, dyz, dxz, dx2–y2, dz2).
    - Similar to other orbitals, d orbitals from different principal electronic shells **:red[differ in size.]**
    - d orbitals are **:red[directional.]**
        - The dxy, dyz and dxz orbitals each consists of 4 lobes of high electron density lying in the xy, yz and zx planes respectively. For example, in the case of dxy orbital, the dxy orbital has 4 lobes that lie in the xy plane in between the x and y axis.
        - The dx2–y2 orbital has 4 lobes of high electron density that lie along the axes of x and y.
        - The dz2 orbital has two lobes along the z axis with a ring of high electron density in the xy plane.
    """
    )
    as_d_orbitals = Image.open("./pages/Images/Dorbitals.png")
    st.image(as_d_orbitals)
with col6:
    as_electronic_configuration = st.button("Electronic Configurations")
if as_electronic_configuration:
    st.markdown("**:blue[Principles of Filling Orbitals]**")
    st.markdown("**Aufbau's Principle**")
    st.markdown(
    """
    - Electrons occupy the orbitals with the **:red[lowest possible energy]** first. 
    - This is because electrons that are closer to the nucleus are more strongly attracted to it. The potential energy will be lower and the system will be more stable. 
    - When the electrons in an atom occupy orbitals of lowest available energy, the atom is said to be in its ground state.
    """
    )
    as_aufbau = Image.open("./pages/Images/aufbau.png")
    st.image(as_aufbau)
    st.markdown("**Pauli Exclusion Principle**")
    st.markdown(
    """
    - Each orbital can hold a **:red[maximum of 2 electrons.]**
    - The two electrons must have **:red[opposte spins]**
    """
    )
    as_pauli = Image.open("./pages/Images/pauli.png")
    st.image(as_pauli)
    st.markdown("**Hund's Rule**")
    st.markdown(
    """
    - When filling a set of degenerate orbitals, electrons occupy the orbitals **:red[singly with parallel spins]** before any pairing occurs. 
    - This is because electrons tend to be as far apart as possible to **:red[minimise inter–electronic repulsion]**
    """
    )
    as_hunds = Image.open("./pages/Images/hunds.png")
    st.image(as_hunds)
    st.markdown("**:blue[Representing Electronic Configuration:]**")
    st.markdown("**Energy Level Diagram**")
    as_energy_level_diagram = Image.open("./pages/Images/EnergyLevelSodium.png")
    st.image(as_energy_level_diagram)
    st.markdown("**Using 'electrons-in-boxes' method**")
    as_electron_in_boxes = Image.open("./pages/Images/electroninboxes.png")
    st.image(as_electron_in_boxes)
    st.markdown("**spdf Notations**")
    as_spdf = Image.open("./pages/Images/spdfnotation.png")
    st.image(as_spdf)
    st.markdown("**Filling more than 18 electrons**")
    st.markdown("**:red[4s orbitals are filled (and removed first) before 3d orbitals]**")
    as_18_config = Image.open("./pages/Images/18electronconfig.png")
    st.image(as_18_config)
    st.markdown("**:blue[Anomalous Electronic Configuration:]**")
    st.markdown("Chromium: [Ar] **3d5**4s1")
    st.markdown("Copper: [Ar]**3d10**4s1")
    
st.divider()


# Show Prompt
#if question:
    #response = ask_GPT(question_template.format(topic = question))
    #st.write(response)


with st.container():
    question = st.chat_input("Enter your prompt here: ")
    if question:
        with st.chat_message("user"):
            st.markdown(f"Q: {question}")
            response = ask_GPT(question)
            st.write(f"A: {response}")


