import { useState } from 'react'
import { rj, useRunRj } from 'react-rocketjump'
import { ajax } from 'rxjs/ajax'
import { useAuthActions, useAuthUser } from 'use-eazy-auth'
import GarmentCard from '../components/GarmentCard'

const itemsState = rj({
  effectCaller: rj.configured(),
  effect: (token) => (search = '') =>
    ajax.getJSON(`/garments/?search=${search}`, {
      Authorization: `Bearer ${token}`,
    }),
})

export default function GarmentBook() {
  const { user } = useAuthUser()
  const { logout } = useAuthActions()
  const [search, setSearch] = useState('')
  const [{ data: items }] = useRunRj(itemsState, [search], false)

  return (
    <div className="row mt-2 p-2">
      <div className="col-md-6 offset-md-3">
        <div className="mb-3 text-center">
          <h1>
            📒 Garment App of <i>@{user.username}</i>
          </h1>
        </div>
        <div className="text-right">
          <button onClick={logout} className="btn btn-light">
            Log Out
          </button>
        </div>
        <div className="mt-2">
          <input
            value={search}
            onChange={e => setSearch(e.target.value)}
            placeholder="Search for a contact"
            style={{ fontSize: 22 }}
            className="form-control"
          />
        </div>
        <div className='list-item mt-5'>
		{console.log(items)}
		  {items &&  
            items.map((item) => (
			 
			 <GarmentCard key={item._id} item={item} />
            ))}
        </div>
      </div>
    </div>
  )
}