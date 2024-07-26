from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from src.auth.schemas import RoleEnum
from src.contacts.schemas import ContactCreate, ContactUpdate, ContactResponse
from src.contacts.repo import ContactRepository
from config.db import get_db
from src.auth.utils import get_current_user, RoleChecker

router = APIRouter()

@router.post("/", response_model=ContactResponse, dependencies=[Depends(RoleChecker([RoleEnum.USER, RoleEnum.ADMIN]))])
async def create_contact(
    contact_create: ContactCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    contact_repo = ContactRepository(db)
    return await contact_repo.create_contact(contact_create, current_user.id)

@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contact(
    contact_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    contact_repo = ContactRepository(db)
    contact = await contact_repo.get_contact(contact_id, current_user.id)
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found"
        )
    return contact

@router.get("/", response_model=list[ContactResponse])
async def get_contacts(
    skip: int = 0,
    limit: int = 10,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    contact_repo = ContactRepository(db)
    return await contact_repo.get_contacts(current_user.id, skip, limit)


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(
    contact_id: int,
    contact_update: ContactUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    contact_repo = ContactRepository(db)
    contact = await contact_repo.get_contact(contact_id, current_user.id)
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found"
        )
    return await contact_repo.update_contact(contact_id, contact_update, current_user.id)

@router.delete("/{contact_id}")
async def delete_contact(
    contact_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    contact_repo = ContactRepository(db)
    contact = await contact_repo.get_contact(contact_id, current_user.id)
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found"
        )
    await contact_repo.delete_contact(contact_id, current_user.id)
    return {"detail": "Contact deleted"}

@router.get("/all/", response_model=list[ContactResponse], dependencies=[Depends(RoleChecker([RoleEnum.ADMIN]))], tags=['admin'])
async def get_all_contacts(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    contact_repo = ContactRepository(db)
    return await contact_repo.get_all_contacts( skip, limit)