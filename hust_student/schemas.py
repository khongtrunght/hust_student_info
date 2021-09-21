from typing import Any, List, Dict, Optional

from pydantic import BaseModel, validator


class Student(BaseModel):
    id: Optional[int] = None
    studentId: Optional[str] = None
    fullName: Optional[str] = None
    password: Optional[str] = None
    birthdate: Optional[int] = None
    birthdateStr: Optional[str] = None
    birthPlace: Optional[str] = None
    departmentId: Optional[int] = None
    programId: Optional[int] = None
    majorId: Optional[int] = None
    majorName: Optional[str] = None
    majorCode: Optional[str] = None
    studentYear: Optional[str] = None
    year: Optional[int] = None
    gender: Optional[int] = None
    tokenKey: Optional[str] = None
    phoneNumber: Optional[str] = None
    englishInfo: Optional[str] = None
    creditInfo: Optional[str] = None
    cpa: Optional[float] = None
    totalCredit: Optional[int] = None
    graduationDate: Optional[int] = None
    email: Optional[str] = None
    personalEmail: Optional[str] = None
    idNumber: Optional[str] = None
    idNumberPlace: Optional[str] = None
    idNumberDate: Optional[int] = None
    lastLoggedIn: Optional[int] = None
    status: Optional[int] = None
    rootId: Optional[int] = None
    uniId: Optional[int] = None
    classId: Optional[int] = None
    lastSemester: Optional[str] = None
    semesters: Optional[List[str]] = None
    classOrder: Optional[int] = None
    cvUrl: Optional[str] = None
    avatarUrl: Optional[str] = None
    className: Optional[str] = None
    companyName: Optional[str] = None
    scholarShip: Optional[str] = None
    position: Optional[str] = None
    notes: Optional[str] = None
    address: Optional[str] = None
    countryId: Optional[int] = None
    countryName: Optional[str] = None
    provinceId: Optional[int] = None
    districtId: Optional[int] = None
    communeId: Optional[int] = None
    homeCommune: Optional[str] = None
    homeDistrict: Optional[str] = None
    homeProvince: Optional[str] = None
    homeAddress: Optional[str] = None
    facebookToken: Optional[str] = None
    studyMode: Optional[int] = None
    studentType: Optional[str] = None
    profileUrl: Optional[str] = None
    facebookId: Optional[str] = None
    relatedEmail: Optional[str] = None
    createdDate: Optional[int] = None
    lastUpdate: Optional[int] = None
    tmpState: Optional[int] = None
    schoolName: Optional[str] = None
    facebookName: Optional[str] = None
    sessionId: Optional[Any] = None
    project: Optional[Any] = None
    trainings: Optional[List] = None
    staffAwards: Optional[List] = None
    relatives: Optional[List] = None
    studentClass: Optional[Any] = None
    schoolUnit: Optional[Any] = None
    major: Optional[Any] = None
    program: Optional[Any] = None
    available: Optional[bool] = None
    allEmails: Optional[List[str]] = None
    profileComplete: Optional[bool] = None


class Teacher(BaseModel):
    id: int
    userName: str
    password: str
    fullName: str
    firstName: str
    lastName: str
    gender: int
    staffCode: str
    commonName: str
    title: int
    degree: int
    jobType: int
    contractType: int
    contractNotes: str
    position: int
    departmentId: int
    rootId: int
    uniId: int
    source: int
    semesters: List
    taxNumber: str
    notes: str
    idNumber: str
    idNumberPlace: str
    idNumberPlaceId: int
    idNumberDate: int
    assuranceNumber: str
    assuranceDate: int
    stateOfficialDate: int
    prevHiredDate: int
    prevPosition: str
    prevCompany: str
    hiredDate: int
    hiredPosition: str
    nickName: str
    qlnnId: int
    llctId: int
    itLevelId: int
    seniorityDate: int
    refCode: str
    bankAccount: str
    bankInfo: str
    website: str
    researchBio: str
    personalBio: str
    profileUrl: str
    candidateGroup: Any
    researchPlan: str
    researchResume: str
    birthDate: int
    birthPlace: str
    birthPlaceId: int
    birthDateStr: str
    workEmail: str
    personalEmail: str
    workPhoneNumber: str
    cellPhoneNumber: str
    otherEmails: List[str]
    otherPhoneNumbers: List[str]
    workAddress: str
    homeAddress: str
    bloodType: str
    priorityTypeId: int
    familyPolicyId: int
    highSchoolEduId: int
    familyOriginId: int
    healthType: int
    residentAddress: str
    residentCountryId: int
    residentProvinceId: int
    residentDistrictId: int
    residentCommuneId: int
    homeTownAddress: str
    homeTownCountryId: int
    homeTownProvinceId: int
    homeTownDistrictId: int
    homeTownCommuneId: int
    partyDate: int
    officialPartyDate: int
    enlistmentDate: int
    dischargeDate: int
    marriedStatus: int
    info: str
    facebookToken: str
    facebookId: str
    facebookName: str
    relatedEmail: str
    lastLoggedIn: int
    avatarUrl: str
    projectStatus: int
    activated: int
    roomId: int
    roomName: str
    probation: int
    probationFrom: int
    probationTo: int
    salaryRaiseDate: int
    status: int
    tmpStatus: int
    tokenKey: str
    currentRoleId: int
    pv: float
    pvExternal: float
    nc: float
    kNc: float
    kVt: float
    extCoeff: float
    roleIds: List
    nation: str
    religion: str
    docUrls: List
    mainResearchTopics: List
    relatedResearchTopics: List
    contracts: List
    roles: List
    sessionId: str
    itemIdList: List
    courseList: List
    projectRequests: List
    quotas: List
    quotasMap: Dict[str, Any]
    currentRole: Any
    rootUnit: Any
    parentUnit: Any
    staffPositions: List
    staffAwards: List
    staffDisciplines: List
    salaryLevels: List
    relatives: List
    trainings: List
    travels: List
    experiences: List
    interruptions: List
    certificates: List
    languageLevels: List
    personTitles: List
    publications: List
    researchProjects: List
    patterns: List
    classes: List
    titleItem: Any
    contractTypeItem: Any
    degreeItem: Any
    jobTypeItem: Any
    salary: Any
    tmpRoles: List
    mainResearchDomainItems: List
    relatedResearchDomainItems: List
    admin: bool
    superAdmin: bool
    roleLeve: int
    roleSchool: bool
    roleUniversity: bool
    roleDepartment: bool
    eduType: int
    subjectIds: List
    vipAdmin: bool
    availableForSalary: bool
    gd: float
    adminUnitId: int
    adminProgramIds: List
    candidate: bool
    candidateRejected: bool
    candidatePreparing: bool
    candidateSubmitted: bool
    candidateApproved: bool
    candidateStatusName: str
    adminQLNguyenVong: bool
    adminStudentClass: bool
    adminClass: bool
    adminPostGrad: bool
    adminUnderGrad: bool
    invited: bool
    externalInvited: bool
    off: bool
    official: bool
    dead: bool
    assistant: bool
    cbkt: bool
    cbhc: bool
    kcd: float
    allEmails: List[str]
    titleFullName: str
    fullTitle: str
    languages: str
    managerUni: bool
    managerSchool: bool

class TeacherDB(BaseModel):
    id: int
    userName: str
    password: str
    fullName: str
    firstName: str
    lastName: str
    gender: int
    staffCode: str
    commonName: str
    title: int
    degree: int
    jobType: int
    contractType: int
    contractNotes: str
    position: int
    departmentId: int
    rootId: int
    uniId: int
    source: int
    taxNumber: str
    notes: str
    idNumber: str
    idNumberPlace: str
    idNumberPlaceId: int
    idNumberDate: int
    assuranceNumber: str
    assuranceDate: int
    stateOfficialDate: int
    prevHiredDate: int
    prevPosition: str
    prevCompany: str
    hiredDate: int
    hiredPosition: str
    nickName: str
    qlnnId: int
    llctId: int
    itLevelId: int
    seniorityDate: int
    refCode: str
    bankAccount: str
    bankInfo: str
    website: str
    researchBio: str
    personalBio: str
    profileUrl: str
    candidateGroup: Any
    researchPlan: str
    researchResume: str
    birthDate: int
    birthPlace: str
    birthPlaceId: int
    birthDateStr: str
    workEmail: str
    personalEmail: str
    workPhoneNumber: str
    cellPhoneNumber: str
    workAddress: str
    homeAddress: str
    bloodType: str
    priorityTypeId: int
    familyPolicyId: int
    highSchoolEduId: int
    familyOriginId: int
    healthType: int
    residentAddress: str
    residentCountryId: int
    residentProvinceId: int
    residentDistrictId: int
    residentCommuneId: int
    homeTownAddress: str
    homeTownCountryId: int
    homeTownProvinceId: int
    homeTownDistrictId: int
    homeTownCommuneId: int
    partyDate: int
    officialPartyDate: int
    enlistmentDate: int
    dischargeDate: int
    marriedStatus: int
    info: str
    facebookToken: str
    facebookId: str
    facebookName: str
    relatedEmail: str
    lastLoggedIn: int
    avatarUrl: str
    projectStatus: int
    activated: int
    roomId: int
    roomName: str
    probation: int
    probationFrom: int
    probationTo: int
    salaryRaiseDate: int
    status: int
    tmpStatus: int
    tokenKey: str
    currentRoleId: int
    pv: float
    pvExternal: float
    nc: float
    kNc: float
    kVt: float
    extCoeff: float
    nation: str
    religion: str
    sessionId: str
    currentRole: Any
    rootUnit: Any
    parentUnit: Any
    titleItem: Any
    contractTypeItem: Any
    degreeItem: Any
    jobTypeItem: Any
    salary: Any
    admin: bool
    superAdmin: bool
    roleLeve: int
    roleSchool: bool
    roleUniversity: bool
    roleDepartment: bool
    eduType: int
    vipAdmin: bool
    availableForSalary: bool
    gd: float
    adminUnitId: int
    candidate: bool
    candidateRejected: bool
    candidatePreparing: bool
    candidateSubmitted: bool
    candidateApproved: bool
    candidateStatusName: str
    adminQLNguyenVong: bool
    adminStudentClass: bool
    adminClass: bool
    adminPostGrad: bool
    adminUnderGrad: bool
    invited: bool
    externalInvited: bool
    off: bool
    official: bool
    dead: bool
    assistant: bool
    cbkt: bool
    cbhc: bool
    kcd: float
    titleFullName: str
    fullTitle: str
    languages: str
    managerUni: bool
    managerSchool: bool

class RootUnit(BaseModel):
    id: int
    parentId: int
    parentName: str
    type: int
    status: int
    functionType: int
    rootId: int
    order: int
    api: int
    unitId: str
    logo: str
    name: str
    nameEn: str
    shortNameVi: str
    shortNameEn: str
    abbrName: str
    commonName: str
    description: str
    website: str
    phoneNumber: str
    faxNumber: str
    email: str
    address: str
    unitCode: str
    coursePrefixes: List[str]
    staffNum: int
    nameHints: List[str]
    invitedTeacherIds: List[int]
    majorCodes: List[str]
    childEducationUnits: List
    teachers: List
    facilityStaffs: List
    majors: List
    displayName: str
    closed: bool
    school: bool
    university: bool
    department: bool
    teachingAndResearch: bool
    teaching: bool


class RootUnitDB(BaseModel):
    id: int
    parentId: int
    parentName: str
    type: int
    status: int
    functionType: int
    rootId: int
    order: int
    api: int
    unitId: str
    logo: str
    name: str
    nameEn: str
    shortNameVi: str
    shortNameEn: str
    abbrName: str
    commonName: str
    description: str
    website: str
    phoneNumber: str
    faxNumber: str
    email: str
    address: str
    unitCode: str
    staffNum: int
    displayName: str
    closed: bool
    school: bool
    university: bool
    department: bool
    teachingAndResearch: bool
    teaching: bool

class Class(BaseModel):
    id: int
    name: str
    studentYear: str
    year: int
    rootId: int
    teacherId: int
    monitorId: str
    secretaryId: str
    programId: int
    status: int
    studentNum: int
    notes: str
    students: List[Student]
    teacher: Optional[Teacher]
    monitor: Any
    secretary: Any
    rootUnit: RootUnit

class ClassDB(BaseModel):
    id: int
    name: str
    studentYear: str
    year: int
    rootId: int
    teacherId: Optional[int]
    monitorId: str
    secretaryId: str
    programId: int
    status: int
    studentNum: int
    notes: str
    monitor: Any
    secretary: Any

    @validator('teacherId')
    def not_minus_one(cls, v):
        if v == -1:
            return None
        else:
            return v




class ClassResp(BaseModel):
    data: Class
    status: int


class StudentResp(BaseModel):
    data: Student
    status: int
