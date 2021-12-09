export default function GarmentCard({ item }) {
  
  console.log(item);
  
  return (
    
	<div className="list-group-item">
       {item.product_id && (
	  <div>
        <span className="mr-3">&#127380;</span>
        <b>{item.product_id}</b>
	   </div>
	   )}
	   {item.product_description && (
      <div>
        <span className="mr-3">&#128214;</span>
        <b>{item.product_description}</b>
      </div>
	   )}
      {item.gender && (
        <div>
          <span className="mr-3">&#128107;</span>
          <b>{item.gender}</b>
        </div>
      )}
      {item.stock && <p className='mb-0 mt-2'>&#9989;{item.stock}</p>}
    </div>
  )
}